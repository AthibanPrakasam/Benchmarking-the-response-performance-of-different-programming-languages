package com.example.demo;

import java.util.HashMap;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ProcessController {

    // POST endpoint to process JSON payload
    @PostMapping("/process")
    public Map<String, Object> process(@RequestBody Map<String, Object> payload) {
        Map<String, Object> response = new HashMap<>();
        response.put("language", "java");
        response.put("message", "Processed successfully");
        return response;
    }

    // GET endpoint to check service health
    @GetMapping("/process")
    public Map<String, Object> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("language", "java");
        response.put("message", "Java service is running");
        return response;
    }
}
