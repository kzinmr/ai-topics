---
title: "Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code"
date: 2026-06-26
processed_at: 2026-06-26T07:12:34.933601+00:00
source_label: "uid=285"
tags: [newsletter, raw]
---

# Newsletter Digest - 2026-06-26

**Subject:** Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
**Collected:** 2026-06-26T07:12:34.933607+00:00
**Articles linked:** 20

## 1. Link

- **URL:** https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zaW1vbncuc3Vic3RhY2suY29tL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj0yZmx4NiZuZXh0PWh0dHBzJTNBJTJGJTJGc2ltb253LnN1YnN0YWNrLmNvbSUyRnAlMkZwb3J0aW5nLXRoZS1tb2ViaXVzLTAyYi1pbWFnZS1pbnBhaW50aW5nIiwicCI6MjAzNjU0NTM4LCJzIjoxMTczMzg2LCJmIjp0cnVlLCJ1Ijo0MDg3NDgyLCJpYXQiOjE3ODI0NTEzNDUsImV4cCI6MjA5ODAyNzM0NSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.MwoHLI5QgbJIqEEkTWT8dXcFujnzLE5-kfvm6UXpDco?

## 2. Link

- **URL:** https://substack.com/app-link/post?publication_id=1173386&post_id=203654538&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDM2NTQ1MzgsImlhdCI6MTc4MjQ1MTM0NSwiZXhwIjoxNzg1MDQzMzQ1LCJpc3MiOiJwdWItMTE3MzM4NiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.KvRLAojZGoXVOCy-UtQq-7JBDGa6T1Xa18pbcHW1GYk

## 3. Link

- **URL:** https://substack.com/@simonw

## 4. Link

- **URL:** https://substack.com/app-link/post?publication_id=1173386&post_id=203654538&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDM2NTQ1MzgsInJlYWN0aW9uIjoi4p2kIiwiaWF0IjoxNzgyNDUxMzQ1LCJleHAiOjE3ODUwNDMzNDUsImlzcyI6InB1Yi0xMTczMzg2Iiwic3ViIjoicmVhY3Rpb24ifQ.VGNnjfCWfakJCew6xwPHq_lqvYR13hAuuMuOuA3oz1A&utm_medium=email&utm_campaign=email-reaction&r=2flx6

## 5. Link

- **URL:** https://substack.com/app-link/post?publication_id=1173386&post_id=203654538&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDM2NTQ1MzgsImlhdCI6MTc4MjQ1MTM0NSwiZXhwIjoxNzg1MDQzMzQ1LCJpc3MiOiJwdWItMTE3MzM4NiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.KvRLAojZGoXVOCy-UtQq-7JBDGa6T1Xa18pbcHW1GYk&r=2flx6&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email

## 6. Link

- **URL:** https://substack.com/app-link/post?publication_id=1173386&post_id=203654538&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDM2NTQ1MzgsImlhdCI6MTc4MjQ1MTM0NSwiZXhwIjoxNzg1MDQzMzQ1LCJpc3MiOiJwdWItMTE3MzM4NiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.KvRLAojZGoXVOCy-UtQq-7JBDGa6T1Xa18pbcHW1GYk

## 7. Link

- **URL:** https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvc2ltb253L3AvcG9ydGluZy10aGUtbW9lYml1cy0wMmItaW1hZ2UtaW5wYWludGluZz91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9MmZseDYmdG9rZW49ZXlKMWMyVnlYMmxrSWpvME1EZzNORGd5TENKd2IzTjBYMmxrSWpveU1ETTJOVFExTXpnc0ltbGhkQ0k2TVRjNE1qUTFNVE0wTlN3aVpYaHdJam94TnpnMU1EUXpNelExTENKcGMzTWlPaUp3ZFdJdE1URTNNek00TmlJc0luTjFZaUk2SW5CdmMzUXRjbVZoWTNScGIyNGlmUS5LdlJMQW9qWkdvWFZPQ3ktVXRRcS03SkJER2E2VDFYYTE4cGJjSFcxR1lrIiwicCI6MjAzNjU0NTM4LCJzIjoxMTczMzg2LCJmIjp0cnVlLCJ1Ijo0MDg3NDgyLCJpYXQiOjE3ODI0NTEzNDUsImV4cCI6MjA5ODAyNzM0NSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.utMDBkwdL5YM-7mldq4oSo4kW85nqhMhOErV8F_FYKM?&utm_source=substack&utm_medium=email

## 8. Link

- **URL:** https://open.substack.com/pub/simonw/p/porting-the-moebius-02b-image-inpainting?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app

## 9. Link

- **URL:** https://substack.com/redirect/875a1711-4e60-4415-b815-0a9d9fa1f00c?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 10. Link

- **URL:** https://substack.com/redirect/e51a9ecf-70d0-4a1b-bf20-485a2dce9f8f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 11. Link

- **URL:** https://substack.com/redirect/3a9be7e0-982b-4374-a321-3c084c3779ef?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 12. Link

- **URL:** https://substack.com/redirect/d7c3703d-f49b-4057-8e2e-443291e061db?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 13. Link

- **URL:** https://substack.com/redirect/f68306fd-cfca-41a5-98ac-d0138a125c4a?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 14. Link

- **URL:** https://substack.com/redirect/0fbac209-04d3-4ded-8fce-8728507ee10e?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 15. Link

- **URL:** https://substack.com/redirect/6069c680-d0df-4142-8ffd-7fc1ffbc77b7?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 16. Link

- **URL:** https://substack.com/redirect/428eee3b-8a03-4ea6-b407-8590eca1ec3b?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 17. Link

- **URL:** https://substack.com/redirect/d35ca3ae-189b-426d-9d57-22b0a3ed9b31?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 18. Link

- **URL:** https://substack.com/redirect/693636c6-7a7f-4514-9fc9-4ccc865d0a5d?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 19. Link

- **URL:** https://substack.com/redirect/7875c556-0450-4ffa-86d6-040878ce870c?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 20. Link

- **URL:** https://substack.com/redirect/c1dfda2e-2370-43ac-b75d-de060bb80bc6?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

