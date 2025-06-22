FROM python:3.13-slim
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app
RUN pip install --upgrade pip
RUN pip install build
RUN python -m build
RUN pip install dist/*.whl
CMD ["python", "src/bot.py"]