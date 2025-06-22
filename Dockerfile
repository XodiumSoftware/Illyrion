FROM python:3.13-slim
VOLUME ["/data"]
WORKDIR /app
COPY src/ ./src/
COPY pyproject.toml ./
ENV PYTHONPATH=/app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir build && \
    python -m build && \
    pip install --no-cache-dir dist/*.whl
CMD ["python", "src/bot.py"]