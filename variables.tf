variable "region" {
  description = "region"
  type = string
}
variable "eks_cluster_name" {
  type = string
}
variable "eks_cluster_policy_arn" {
  type = string
}
variable "eks_vpc_controller_policy_arn" {
  type = string
}
variable "node_group_subnet_ids" {
  type = list(any)
}
variable "cluster_subnet_ids" {
  type = list(any)
}
variable "eks_worker_node_policy_arn" {
  type = string
}
variable "eks_cni_policy_arn" {
  type = string
}
variable "container_registry_arn" {
  type = string
}
variable "node_group_name" {
  type = string
}
variable "eks_node_desired_size" {
  type = number
}
variable "eks_node_max_size" {
  type = number
}
variable "eks_node_min_size" {
  type = number
}
variable "eks_node_max_unavailable" {
  type =  number
}

variable "instance_types" {
  type = list
}