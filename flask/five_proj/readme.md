# Commands to build docker image
docker build -t fixedallvul .
# Verify docker images
docker images
# Scan Image for Vulnerabilities (HIGH & CRITICAL)
# Using Trivy (Aqua Security vulnerability scanner):
trivy image --severity HIGH,CRITICAL fixedallvul:latest
