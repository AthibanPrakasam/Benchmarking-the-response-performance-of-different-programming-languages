package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	r.GET("/process", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"language": "go",
			"message":  "GET /process is alive",
		})
	})

	r.POST("/process", func(c *gin.Context) {
		var payload map[string]interface{}
		if err := c.BindJSON(&payload); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid JSON"})
			return
		}
		c.JSON(http.StatusOK, gin.H{
			"language": "go",
			"message":  "Processed successfully",
		})
	})

	r.Run(":8002")
}
