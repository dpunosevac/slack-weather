resource "aws_api_gateway_rest_api" "weather_api" {
  name = "weatherAPI"
  description = "Serverless weather API"
}

resource "aws_api_gateway_resource" "weather_api_resource" {
  rest_api_id = "${aws_api_gateway_rest_api.weather_api.id}"
  parent_id = "${aws_api_gateway_rest_api.weather_api.root_resource_id}"
  path_part = "weather"
}

resource "aws_api_gateway_method" "weather_api_method" {
  rest_api_id = "${aws_api_gateway_rest_api.weather_api.id}"
  resource_id = "${aws_api_gateway_resource.weather_api_resource.id}"
  http_method = "POST"
  authorization = "NONE"
  request_parameters = { "method.request.header.
}

resource "aws_api_gateway_integration" "weather_api_method-integration" {
  rest_api_id = "${aws_api_gateway_rest_api.weather_api.id}"
  resource_id = "${aws_api_gateway_resource.weather_api_resource.id}"
  http_method = "${aws_api_gateway_method.weather_api_method.http_method}"
  type = "AWS_PROXY"
  uri = "${aws_lambda_function.lambda.invoke_arn}"
  integration_http_method = "POST"
}

resource "aws_lambda_permission" "allow_weather_api_method" {
  function_name = "${aws_lambda_function.lambda.function_name}"
  statement_id = "allow_weather_api_method"
  action = "lambda:InvokeFunction"
  principal = "apigateway.amazonaws.com"
  source_arn = "${aws_api_gateway_rest_api.weather_api.execution_arn}/*/*/*"
}
