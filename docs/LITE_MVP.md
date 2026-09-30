# Lite MVP

## Objective

Reduce the sales rep's manual email review burden by turning a merchant submission into one actionable Slack notification.

## Input

- Merchant name
- Email subject
- Attachment filenames

## Output

- recognized document types
- missing required documents
- unknown/unclassified attachments
- Slack-formatted notification

## Human-in-the-loop

Sales reviews the Slack output and contacts the merchant manually.

## Explicit non-goals

- KYB approval/rejection
- public registry verification
- autonomous merchant email
- risk scoring
- full OCR/LLM production integration

## Next upgrade

Replace filename classification with a document parser/OCR + versioned LLM classifier, while keeping the checklist and notification contracts stable.
