---
title: "AWS Challenger: Trainium3 Inference and Microarchitecture Deep Dive"
date: 2026-11-27
processed_at: 2026-11-28T10:18:49.731859+00:00
source_label: "uid=947"
tags: [newsletter, raw]
---

# Newsletter Digest - 2026-11-27

**Subject:** AWS Challenger: Trainium3 Inference and Microarchitecture Deep Dive
**Collected:** 2026-11-28T10:18:49.731869+00:00
**Articles linked:** 20

## 1. Link

- **URL:** https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9uZXdzbGV0dGVyLnNlbWlhbmFseXNpcy5jb20vc3Vic2NyaWJlP3V0bV9zb3VyY2U9ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXN1YnNjcmliZSZyPTJmbHg2Jm5leHQ9aHR0cHMlM0ElMkYlMkZuZXdzbGV0dGVyLnNlbWlhbmFseXNpcy5jb20lMkZwJTJGdHJhaW5pdW0zLWluZmVyZW5jZXgiLCJwIjoyMjYyODE2NTMsInMiOjYzNDk0OTIsImYiOnRydWUsInUiOjQwODc0ODIsImlhdCI6MTc5NTc5NTEzNCwiZXhwIjoyMTExMzcxMTM0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.hY50cNEhqEPCWP8n_Zm0K0gfewdpytjra390BcUruvA?

## 2. Link

- **URL:** https://substack.com/app-link/post?publication_id=6349492&post_id=226281653&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMjYyODE2NTMsImlhdCI6MTc5NTc5NTEzNCwiZXhwIjoxNzk4Mzg3MTM0LCJpc3MiOiJwdWItNjM0OTQ5MiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.GI56B5y63u0YmCoN5WCJ8umeRuGg_TUAeN9QUOCsrAI

## 3. Link

- **URL:** https://substack.com/@kimbobachen

## 4. Link

- **URL:** https://substack.com/@rottencheese

## 5. Link

- **URL:** https://substack.com/@wenyaogao

## 6. Link

- **URL:** https://substack.com/@camjquilici

## 7. Link

- **URL:** https://substack.com/@adibarrasemi

## 8. Link

- **URL:** https://substack.com/@danielnishball730869

## 9. Link

- **URL:** https://substack.com/@tonysung2

## 10. Link

- **URL:** https://substack.com/@semianalysis

## 11. Link

- **URL:** https://substack.com/app-link/post?publication_id=6349492&post_id=226281653&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMjYyODE2NTMsInJlYWN0aW9uIjoi4p2kIiwiaWF0IjoxNzk1Nzk1MTM0LCJleHAiOjE3OTgzODcxMzQsImlzcyI6InB1Yi02MzQ5NDkyIiwic3ViIjoicmVhY3Rpb24ifQ.FN4f1J8OUK6HQXRkZ6gw4K1Odh5VnQH_lwxq03R4YHE&utm_medium=email&utm_campaign=email-reaction&r=2flx6

## 12. Link

- **URL:** https://substack.com/app-link/post?publication_id=6349492&post_id=226281653&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMjYyODE2NTMsImlhdCI6MTc5NTc5NTEzNCwiZXhwIjoxNzk4Mzg3MTM0LCJpc3MiOiJwdWItNjM0OTQ5MiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.GI56B5y63u0YmCoN5WCJ8umeRuGg_TUAeN9QUOCsrAI&r=2flx6&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email

## 13. Link

- **URL:** https://substack.com/app-link/post?publication_id=6349492&post_id=226281653&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMjYyODE2NTMsImlhdCI6MTc5NTc5NTEzNCwiZXhwIjoxNzk4Mzg3MTM0LCJpc3MiOiJwdWItNjM0OTQ5MiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.GI56B5y63u0YmCoN5WCJ8umeRuGg_TUAeN9QUOCsrAI

## 14. Link

- **URL:** https://open.substack.com/pub/semianalysis/p/trainium3-inferencex?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&action=restack-comment&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMjYyODE2NTMsImlhdCI6MTc5NTc5NTEzNCwiZXhwIjoxNzk4Mzg3MTM0LCJpc3MiOiJwdWItNjM0OTQ5MiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.GI56B5y63u0YmCoN5WCJ8umeRuGg_TUAeN9QUOCsrAI&utm_source=substack&utm_medium=email

## 15. Link

- **URL:** https://open.substack.com/pub/semianalysis/p/trainium3-inferencex?utm_source=email&redirect=app-store-no-desktop&inbox=true&utm_campaign=email-read-in-app

## 16. Link

- **URL:** https://substack.com/redirect/469a3962-41c9-44ec-b6d2-b5f73e7e213f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 17. Link

- **URL:** https://substack.com/redirect/ca29fa7f-44f8-479b-8f84-1452d6de4d3f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 18. Link

- **URL:** https://substack.com/redirect/9c282685-c640-4dca-bd96-24d7aab0cc84?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 19. Link

- **URL:** https://substack.com/redirect/54d837ed-1e47-43ac-b814-9d0cf0c62aba?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 20. Link

- **URL:** https://substack.com/redirect/e992c505-23b7-433a-afde-69f13aa43ac9?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

