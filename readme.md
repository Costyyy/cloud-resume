CloudFront distribution: d2u6bf6755ez4c.cloudfront.net

Built and deployed personal CV site on AWS.

## Architecture

- **Frontend**: HTML/CSS hosted on S3, served via CloudFront over HTTPS
- **Backend**: API Gateway triggers a Lambda function that reads/increments a visitor counter in DynamoDB
- **Infrastructure**: All AWS resources defined in Terraform
- **CI/CD**: GitHub Actions deploys on every push to main

## Stack

AWS S3, CloudFront, Lambda, DynamoDB, API Gateway, Terraform, GitHub Actions

## Deployment

```bash
cd infra/
terraform init
terraform apply