extends Area2D

@onready var tip_label: Label = $tip_label

func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		tip_label.visible = true

func _on_body_exited(body: Node2D) -> void:
	if body is CharacterBody2D:
		tip_label.visible = false
