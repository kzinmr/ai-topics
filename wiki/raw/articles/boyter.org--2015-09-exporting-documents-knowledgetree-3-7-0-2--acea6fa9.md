---
title: "Exporting Documents from KnowledgeTree 3.7.0.2"
url: "https://boyter.org/2015/09/exporting-documents-knowledgetree-3-7-0-2/"
fetched_at: 2026-05-05T07:02:01.555514+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Exporting Documents from KnowledgeTree 3.7.0.2

Source: https://boyter.org/2015/09/exporting-documents-knowledgetree-3-7-0-2/

I was recently tasked with exporting a large collection of documents from KnowledgeTree (KT) for a client. The collection was too large to use the download all functionality and too wide to attempt to export each folder individually.
I had played around with the WebDav connection that KT provides but it either didn’t work or was designed deliberately to not allow exporting of the documents.
I looked at where the documents were  stored on disk but KT stores them as numbered files in numbered directories sans extension or folder information.
Long story short I spent some time poking through the database to identify the tables which would contain the correct metadata which would allow me to rebuild the tree using a proper filesystem. For record the tables required are the following,
folders – Contains the folder tree. Each entry represents a folder and contains its parent folder id.
documents – Contains the documents that each folder contains. Knowing the folders id you can determine what documents live in that folder.
document_content_version – Contains the metadata required to get the actual file from disk. A 1 to 1 mapping between document id and this table is all that is required.
That said here is a short Python script which can be used to rebuild the folders and documents on disk. All that is required is to ensure that Python MySQLdb is installed and to set the database details. Depending on your KT install you may need to change the document location. Where  the script is run it will replicate the folder tree containing the documents preserving the structures, names and extensions.
Keep in mind this is a fairly ugly script abusing global variables and such. It is also not incredibly efficient, but did manage to extract 20GB of files in my case in a little under 10 minutes.
import
MySQLdb
import
os
import
shutil
# KnowledgeTree default place to store documents
ktdocument
=
'/var/www/ktdms/Documents/'
conn
=
MySQLdb
.
connect(user
=
''
, passwd
=
''
,db
=
''
, charset
=
"utf8"
, use_unicode
=
True
)
cursor
=
conn
.
cursor()
# global variables FTW
cursor
.
execute(
'''select id, parent_id, name from folders;'''
)
allfolders
=
cursor
.
fetchall()
cursor
.
execute(
'''select id, folder_id from documents;'''
)
alldocuments
=
cursor
.
fetchall()
cursor
.
execute(
'''select document_id, filename, storage_path from document_content_version;'''
)
document_locations
=
cursor
.
fetchall()
# create folder tree which matches whatever the database suggests exists
def
create_folder_tree
(parent_id, path):
directories
=
[x
for
x
in
allfolders
if
x[
1
]
==
parent_id]
for
directory
in
directories:
d
=
'.
%s
/
%s
/'
%
(path, directory[
2
])
print d
os
.
makedirs(d)
# get all the files that belong in this directory
for
document
in
[x
for
x
in
alldocuments
if
x[
1
]
==
directory[
0
]]:
try
:
location
=
[x
for
x
in
document_locations
if
document[
0
]
==
x[
0
]][
0
]
print
'copy
%s%s
%s%s
'
%
(ktdocument, location[
2
], d, location[
1
])
shutil
.
copy2(
'
%s%s
'
%
(ktdocument, location[
2
]),
'
%s%s
'
%
(d, location[
1
]))
except
:
print
'ERROR exporting - Usually due to a linked document.'
create_folder_tree(parent_id
=
directory[
0
], path
=
'
%s
/
%s
'
%
(path, directory[
2
]))
create_folder_tree(parent_id
=
1
, path
=
''
)
