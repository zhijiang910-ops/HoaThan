extends Node2D
const VFX = preload("res://SectVFX/SectVFX.gd")
var fx: Node2D
var clock := 0.0
var skill_id := "01_array"
var boundary_done := false
var tail := 0.0
func _ready() -> void:
	get_viewport().transparent_bg = true
	RenderingServer.set_default_clear_color(Color(0,0,0,0))
	var a := OS.get_cmdline_user_args()
	if a.size() > 0: skill_id = a[0]
	fx = VFX.new()
	add_child(fx)
	fx.position = Vector2(300,560)
	var aim := Vector2(240,0)
	var options := {"demo_incoming":false,"show_caster":false}
	if skill_id == "02_beam":
		fx.position.x = 100
		options.contact_offsets = [Vector2(390,0),Vector2(216,0)]
	if skill_id == "01_array":
		fx.position = Vector2(360,610)
		aim = Vector2(200,-90)
	assert(fx.play_skill(skill_id,"east",aim,options)==OK)
func _process(delta: float) -> void:
	clock += delta
	if skill_id == "01_array" and clock > 2 and not boundary_done:
		boundary_done = true
	if (not fx.playing and clock > 0.5) or clock > 13.0:
		tail += delta
		if tail > 0.2: get_tree().quit()
