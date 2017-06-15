#!/bin/bash
curl -H "Content-Type: application/json" -X POST -d '{"device_id": "abc", "face_vector": "1212312312-123123-123-12-312"}' http://localhost:8080/hash/
