---
title: "How to make forbidden changes to SQLite tables"
url: "https://rakhim.exotext.com/how-to-make-forbidden-changes-to-sqlite-tables"
fetched_at: 2026-04-28T07:02:00.713148+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# How to make forbidden changes to SQLite tables

Source: https://rakhim.exotext.com/how-to-make-forbidden-changes-to-sqlite-tables

Sometimes you need to make a change to an SQLite table which is not possible with a simple
ALTER
command. For example, today I realized that
email_verifications
table in my DB references
users
with a foreign key, but does not have
ON DELETE CASCADE
(I simply forgot to put it in). This makes it impossible to delete a record from
users
table if there are corresponding records in
email_verifications
.
There is a
hacky
way to achieve this, but I prefer this:
Create a new table with the correct structure (in my case, with
ON DELETE CASCADE
enabled).
Copy data from the old table to the new table.
Rename the old table.
Rename the new table.
Drop the old table (if everything is ok).
It comes down to:
CREATE TABLE IF NOT EXISTS email_verifications_2 (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    verification_code TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
);

INSERT INTO email_verifications_2 SELECT * FROM email_verifications;

ALTER TABLE email_verifications RENAME TO email_verifications_old;
ALTER TABLE email_verifications_2 RENAME TO email_verifications;
If everything is ok, we can drop the old table now:
DROP TABLE email_verifications_old;
