const sprites = [["luc", 210, 196, 137, 101, 2], ["lam", 509, 248, 125, 128, 1.33], ["tim", 1189, 269, 22, 31, 2], ["do", 1259, 309, 20, 27, 1.33]];
export function mountWisps(scene, {reducedMotion = false} = {}) {
  const layer = document.createElement('div');
  layer.className = 'lobby-wisps';
  layer.setAttribute('aria-hidden','true');
  layer.dataset.reducedMotion = String(reducedMotion);
  for (const [name,x,y,width,height,period] of sprites) {
    const sprite = new Image();
    sprite.alt = '';
    sprite.draggable = false;
    sprite.src = new URL('./assets/' + name + '.png', import.meta.url).href;
    Object.assign(sprite.style, {
      left: x / 1336 * 100 + '%', top: y / 582 * 100 + '%',
      width: width / 1336 * 100 + '%', height: height / 582 * 100 + '%',
      animationDuration: period + 's', animationDelay: -x / 300 + 's'
    });
    layer.append(sprite);
  }
  scene.append(layer);
  return {
    setReducedMotion(on) { layer.dataset.reducedMotion = String(on); },
    destroy() { layer.remove(); }
  };
}
