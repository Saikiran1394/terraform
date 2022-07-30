Comment the lifecycle block in main.tf file to reflect the chages for desired size. This is used for to prevent Terraform from scaling down ASG behind AWS EKS Managed Node Group.
lifecycle { create_before_destroy = true ignore_changes = [ scaling_config[0].desired_size, ] }
