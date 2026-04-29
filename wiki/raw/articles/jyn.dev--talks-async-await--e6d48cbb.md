---
title: "async() => { await }"
url: "https://jyn.dev/talks/async-await/"
fetched_at: 2026-04-29T07:02:12.321468+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# async() => { await }

Source: https://jyn.dev/talks/async-await/

Serving multiple clients at once: concurrency
In ~2010, async code looked like this ("callback hell")
fs.readdir(source, function (err, files) {
		if (err) {
			console.log('Error finding files: ' + err)
		} else {
			files.forEach(function (filename, fileIndex) {
				console.log(filename)
				gm(source + filename).size(function (err, values) {
					if (err) {
						console.log('Error identifying file size: ' + err)
					} else {
						console.log(filename + ' : ' + values)
						aspect = (values.width / values.height)
						widths.forEach(function (width, widthIndex) {
							height = Math.round(width / aspect)
							console.log('resizing ' + filename + 'to ' + height + 'x' + height)
							this.resize(width, height).write(dest + 'w' + width + '_' + filename, function(err) {
								if (err) console.log('Error writing file: ' + err)
							})
						}.bind(this))
					}
				})
			})
		}
	})
