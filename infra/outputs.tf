output "alb_dns_name" {
  description = "Public URL of the load balancer"
  value       = "http://${aws_lb.app.dns_name}"
}

output "rds_endpoint" {
  description = "RDS endpoint (only reachable from inside the VPC, shown for reference)"
  value       = aws_db_instance.postgres.endpoint
}
