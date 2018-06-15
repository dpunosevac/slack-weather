provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region = "${var.region}"
}

provider "archive" {}

data "archive_file" "zip" {
  type = "zip"
  source_file = "weather.py"
  output_path = "weather_serverless.zip"
}

resource "aws_lambda_function" "lambda" {
  function_name = "get_weather"
  
  filename = "${data.archive_file.zip.output_path}"
  source_code_hash = "${data.archive_file.zip.output_sha}"
  role = "${var.role_arn}"

  handler = "weather.weather_handler"
  runtime = "python3.6"

  environment {
    variables = {
      API_KEY = "${var.api_key}"
    }
  }
}

