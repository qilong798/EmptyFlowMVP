extends Node2D

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
		var current_scene_name: String = get_tree().current_scene.name
		if current_scene_name == "world_a":
			get_tree().change_scene_to_file("res://scenes/world_b.tscn")
		else:
			get_tree().change_scene_to_file("res://scenes/world_a.tscn")
