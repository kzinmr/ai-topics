---
title: "Open models recap: more on Kimi K3, Qwen 3.8, Xi's WAIC speech, distillation, the open-closed gap, and what's next"
date: 2026-07-22
processed_at: 2026-07-24T10:20:33.906281+00:00
source_label: "uid=400"
tags: [newsletter, raw]
---

# Newsletter Digest - 2026-07-22

**Subject:** Open models recap: more on Kimi K3, Qwen 3.8, Xi's WAIC speech, distillation, the open-closed gap, and what's next
**Collected:** 2026-07-24T10:20:33.906289+00:00
**Articles linked:** 20

## 1. Link

- **URL:** https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cuaW50ZXJjb25uZWN0cy5haS9zdWJzY3JpYmU_dXRtX3NvdXJjZT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtc3Vic2NyaWJlJnI9MmZseDYmbmV4dD1odHRwcyUzQSUyRiUyRnd3dy5pbnRlcmNvbm5lY3RzLmFpJTJGcCUyRm9wZW4tbW9kZWxzLXJlY2FwLW1vcmUtb24ta2ltaS1rMyIsInAiOjIwNzk2OTYyMCwicyI6NDgyMDYsImYiOnRydWUsInUiOjQwODc0ODIsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoyMTAwMzA1NjQyLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.jv5wkoBg92LFZfnDJnI72jjM37Rx4N79YC42xkOipns?

## 2. Link

- **URL:** https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cuaW50ZXJjb25uZWN0cy5haS9wL29wZW4tbW9kZWxzLXJlY2FwLW1vcmUtb24ta2ltaS1rMz91dG1fY2FtcGFpZ249ZW1haWwtaGFsZi1wb3N0JnI9MmZseDYmdG9rZW49ZXlKMWMyVnlYMmxrSWpvME1EZzNORGd5TENKd2IzTjBYMmxrSWpveU1EYzVOamsyTWpBc0ltbGhkQ0k2TVRjNE5EY3lPVFkwTWl3aVpYaHdJam94TnpnM016SXhOalF5TENKcGMzTWlPaUp3ZFdJdE5EZ3lNRFlpTENKemRXSWlPaUp3YjNOMExYSmxZV04wYVc5dUluMC5xdGE1YmRSUkdRQTZEbHhyLXFOcGp0dlBCZVBlVHJEdUpLY0xFbjBvV0ZzIiwicCI6MjA3OTY5NjIwLCJzIjo0ODIwNiwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzg0NzI5NjQyLCJleHAiOjIxMDAzMDU2NDIsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.H6cDOzU-mkf3A8JEU0NLzdCYNvzmFJ28IGOIDYJUc04?

## 3. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card#play

## 4. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card_show_logo#play

## 5. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card_show_title#play

## 6. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card_post_title#play

## 7. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card_duration#play

## 8. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card_progress_bar#play

## 9. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email&utm_content=play_card_play_button#play

## 10. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_content=listen_now_button

## 11. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs

## 12. Link

- **URL:** https://substack.com/@natolambert

## 13. Link

- **URL:** https://substack.com/@xeophon

## 14. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsInJlYWN0aW9uIjoi4p2kIiwiaWF0IjoxNzg0NzI5NjQyLCJleHAiOjE3ODczMjE2NDIsImlzcyI6InB1Yi00ODIwNiIsInN1YiI6InJlYWN0aW9uIn0.B-dVLQWI6-nnyVCQ_7TANFMYQ591LrE04ix83GJt_g8&utm_medium=email&utm_campaign=email-reaction&r=2flx6

## 15. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&r=2flx6&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email

## 16. Link

- **URL:** https://substack.com/app-link/post?publication_id=48206&post_id=207969620&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs

## 17. Link

- **URL:** https://open.substack.com/pub/robotic/p/open-models-recap-more-on-kimi-k3?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&action=restack-comment&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc5Njk2MjAsImlhdCI6MTc4NDcyOTY0MiwiZXhwIjoxNzg3MzIxNjQyLCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.qta5bdRRGQA6Dlxr-qNpjtvPBePeTrDuJKcLEn0oWFs&utm_source=substack&utm_medium=email

## 18. Link

- **URL:** https://open.substack.com/pub/robotic/p/open-models-recap-more-on-kimi-k3?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app

## 19. Link

- **URL:** https://substack.com/redirect/14611b80-0ca3-44d5-9ba8-a3ac26c9dd23?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

## 20. Link

- **URL:** https://substack.com/redirect/62fdd7f5-4c05-41a6-960c-699364dc4513?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

