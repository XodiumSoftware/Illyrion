FROM python:3.13-slim
VOLUME ["/data"]
WORKDIR /data
COPY src/ /data/src/
COPY pyproject.toml ./
ENV PYTHONPATH=/data
RUN pip install --upgrade pip && \
    pip install --no-cache-dir build && \
    python -m build && \
    pip install --no-cache-dir dist/*.whl
CMD ["python", "src/bot.py"]