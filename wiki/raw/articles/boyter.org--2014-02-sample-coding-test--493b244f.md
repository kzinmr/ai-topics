---
title: "Sample Coding Test"
url: "https://boyter.org/2014/02/sample-coding-test/"
fetched_at: 2026-05-05T07:02:03.730490+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sample Coding Test

Source: https://boyter.org/2014/02/sample-coding-test/

Being in the job market again I been doing quite a few tests. Since I have already put in the effort to a test without result I thought I would post it here.
The test involved producing output from a supplied CSV input file which contained insurance claims. Something about taking the input and using it to predict future claims. Please forgive my explanation as I am not a financial expert. Anyway the idea was to take an input such as the following,
Header
One, 1992, 1992, 110.0
One, 1992, 1993, 170.0
One, 1993, 1993, 200.0
Two, 1990, 1990, 45.2
Two, 1990, 1991, 64.8
Two, 1990, 1993, 37.0
Two, 1991, 1991, 50.0
Two, 1991, 1992, 75.0
Two, 1991, 1993, 25.0
Two, 1992, 1992, 55.0
Two, 1992, 1993, 85.0
Two, 1993, 1993, 100.0
into the following,
1990, 4
One, 0, 0, 0, 0, 0, 0, 0, 110, 280, 200
Two, 45.2, 110, 110, 147, 50, 125, 150, 55, 140, 100
The test was mostly about proving that you can write maintainable code which is unit testable and the like. Anyway here is my solution. It takes in a list of objects which represent each of the four columns of the input.
The feedback I received back was that the coverage I achieved was high (I had a collection of tests over the methods), the code clean and well documented
public
class
TriangleCSVLine
{
public
string
product {
get
;
set
; }
public
int
originYear {
get
;
set
; }
public
int
developmentYear {
get
;
set
; }
public
double
incrementalValue {
get
;
set
; }
}
public
List<
string
> TranslateToOutput(List<TriangleCSVLine> parsedCsv)
{
var
output =
new
List<
string
>();
// Sanity checks...
if
(parsedCsv ==
null
|| parsedCsv.Count ==
0
)
{
return
output;
}
output.Add(GenerateHeader(parsedCsv));
// Used to determine where we are looking
var
totalYears = parsedCsv.Select(x => x.developmentYear).Distinct().OrderBy(x => x);
var
minYear = totalYears.Min();
var
maxYear = totalYears.Max();
foreach
(
var
product
in
parsedCsv.Select(x => x.product).Distinct())
{
// All of the products values and the years it has
var
productValues = parsedCsv.Where(x => product.Equals(x.product));
var
originYears = Enumerable.Range(minYear, (maxYear - minYear) +
1
);
var
values =
new
List<
double
>();
foreach
(
var
year
in
originYears)
{
// For each of the development years for this "period"
var
developmentYears = parsedCsv.Where(x => x.originYear == year)
.Select(x => x.developmentYear).Distinct();
// If we have no development years
// that means we have an origin year without a year 1
// development year. This means we have no idea how many values
// of zero should be in the file, so lets bail
// should probably go into a pre validation
if
(developmentYears.Count() ==
0
)
{
throw
new
MissingOriginDevelopmentTrangleCSVException(
string
.Format(
"Missing development years for origin {0} in product {1}"
, year, product)
);
}
// The values are running values...
// so we keep the total and increment it as we go
double
runningTotal =
0
;
foreach
(
var
rangeYear
in
Enumerable.Range(developmentYears.Min(), (developmentYears.Max() - developmentYears.Min()) +
1
))
{
var
value1 = productValues.Where(x => x.originYear == year && x.developmentYear == rangeYear).SingleOrDefault();
if
(value1 !=
null
)
{
runningTotal += value1.incrementalValue;
}
values.Add(runningTotal);
}
}
output.Add(
string
.Format(
"{0}, {1}"
, product,
string
.Join(
", "
, values)));
}
return
output;
}
private
string
GenerateHeader(List<TriangleCSVLine> parsedCsv)
{
// Get distinct list of all the years
var
years = parsedCsv.Select(x => x.developmentYear).Distinct();
// 1990-1990 counts as 1 year so add one
var
developmentYears = (years.Max() - years.Min()) +
1
;
var
header =
string
.Join(
", "
, years.Min(), developmentYears);
return
header;
}
