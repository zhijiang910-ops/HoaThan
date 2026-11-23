extends Node
var t := 0.0
var fired := false
func _ready() -> void:
	get_viewport().transparent_bg = true
	RenderingServer.set_default_clear_color(Color(0,0,0,0))
func _process(d: float) -> void:
	t += d
	var w = get_parent()
	w.self_modulate.a = 0.0
	if is_instance_valid(w.player) and w.player.animated_sprite: w.player.animated_sprite.visible = false
	for n in w.get_tree().get_nodes_in_group("_x"): pass
	for c in w.find_children("*", "Control", true, false): c.visible = false
	for c in w.find_children("*", "CanvasLayer", true, false): c.visible = false
	if is_instance_valid(w.entities):
		for e in w.entities.get_children():
			if e is StaticBody2D: e.queue_free()
			if e is CharacterBody2D:
				for ch in e.get_children(): if ch is Polygon2D: ch.visible = false
	if not fired and t > 0.5 and w.training and w.training.has_method("request_wanjian_cast"):
		w.player.facing = "east"; w.training.request_wanjian_cast(); fired = true
	if t > 5.5: get_tree().quit()
