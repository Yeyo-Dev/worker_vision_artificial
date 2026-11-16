# YOLO Vision Worker

**An asynchronous computer vision worker for object detection and visual evidence analysis using Python and YOLOv8.**

## Overview

YOLO Vision Worker is a Python-based microservice designed to process visual evidence asynchronously through an event-driven architecture.

The worker uses YOLOv8 for object detection, receives processing tasks through RabbitMQ, analyzes visual inputs and produces structured results that can be consumed by other services.

The project focuses on modularity, asynchronous processing and separation of responsibilities, making it suitable for integration into distributed systems.

## Key Features

- **Object Detection:** Uses YOLOv8 for visual analysis and object identification.
- **Asynchronous Processing:** Processes incoming tasks through RabbitMQ.
- **Event-Driven Architecture:** Decouples visual analysis from the services responsible for collecting evidence.
- **Structured Output:** Generates machine-readable analysis results.
- **Independent Service:** Designed to operate as an isolated worker within a larger microservices architecture.
- **Python-Based:** Uses the Python ecosystem for computer vision and machine learning.

## Architecture

The worker follows a message-driven processing pipeline:

```mermaid
flowchart LR
    A[Message Broker] --> B[Worker Consumer]
    B --> C[Evidence Retrieval]
    C --> D[YOLOv8 Inference]
    D --> E[Result Processing]
    E --> F[Structured Output]
    F --> G[Message Broker]
```

### Processing Workflow

1. **Message Consumption:** Receives a task from the message broker.
2. **Evidence Retrieval:** Obtains the visual input required for analysis.
3. **Inference:** Executes object detection using YOLOv8.
4. **Result Processing:** Interprets detection results and prepares structured evidence.
5. **Message Publishing:** Sends the resulting analysis to the designated output channel.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main development language |
| YOLOv8 | Object detection and inference |
| RabbitMQ | Asynchronous messaging |
| JSON | Structured message exchange |

## Integration

This worker is designed to operate as an independent component within an event-driven architecture.

Its integration with other services follows a producer-consumer communication model:

- An upstream service publishes visual analysis tasks.
- The worker consumes and processes those tasks.
- The resulting evidence is published for downstream processing.

The message contracts and infrastructure configuration must be aligned with the integrating application.

## Project Structure

```text
yolo-vision-worker/
├── main.py
├── worker.py
├── soft_evidence.py
├── requirements.txt
├── README.md
└── .gitignore
```

*The structure above is illustrative and should be adjusted to match the actual repository contents.*

## Development Status

This repository contains an extracted computer vision component originally developed as part of a larger distributed application.

It is being documented and organized as an independent software component.

**Note:** This project is not presented as a complete proctoring application. Its functionality is focused on the visual analysis worker.

## License

See the repository's LICENSE file for licensing and usage terms.
