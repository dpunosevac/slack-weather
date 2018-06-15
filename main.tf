resource "aws_api_gateway_deployment" "example_deployment_prod" {
  depends_on = [
    "aws_api_gateway_method.weather_api_method",
    "aws_api_gateway_integration.weather_api_method-integration"
  ]
  rest_api_id = "${aws_api_gateway_rest_api.weather_api.id}"
  stage_name = "api"
}

output "prod_url" {
  value = "https://${aws_api_gateway_deployment.example_deployment_prod.rest_api_id}.execute-api.${var.region}.amazonaws.com/${aws_api_gateway_deployment.example_deployment_prod.stage_name}/${aws_api_gateway_resource.weather_api_resource.path_part}"
}