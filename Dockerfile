FROM public.ecr.aws/lambda/python:3.8

COPY ./modules/users/requirements.txt ./modules/users/requirements.txt
RUN pip install -r ./modules/users/requirements.txt 