from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.aws.devtools import Codebuild
from diagrams.onprem.vcs import Github

with Diagram("Loan Management System", show=False, direction="TB"):
    github = Github("GitHub")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            with Cluster("Public Subnet"):
                alb = ELB("ALB")
                ecs = ECS("ECS Cluster")

            with Cluster("Private Subnet"):
                rds = RDS("RDS")
                cache = ElastiCache("ElastiCache")
                s3 = S3("S3")

        ecr = Codebuild("ECR")
        cw = Cloudwatch("CloudWatch")

    github >> ecr >> ecs
    alb >> ecs
    ecs >> rds
    ecs >> cache
    ecs >> s3
    ecs - cw