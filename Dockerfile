FROM python:3.13-slim
WORKDIR /app
COPY src/ ./src/
COPY pyproject.toml ./
ENV PYTHONPATH=/app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir build && \
    python -m build && \
    pip install --no-cache-dir dist/*.whl && \
    useradd -m illyrion && \
    chown -R illyrion /app
USER illyrion
EXPOSE 8080
CMD ["python", "src/bot.py"]