local active_border_color = "rgb(fab387)"
local inactive_border_color = "rgb(313244)"

hl.config({
  general = {
    gaps_in = 3,
    gaps_out = 6,
    border_size = 2,
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },

  decoration = {
    rounding = 14,

    active_opacity = 1.0,
    inactive_opacity = 0.95,
    fullscreen_opacity = 1.0,

    shadow = {
      enabled = true,
      range = 25,
      render_power = 3,
      color = "rgba(00000077)",
      offset = "0 4",
    },

    blur = {
      enabled = true,
      size = 6,
      passes = 3,
      contrast = 1.0,
      brightness = 1.1,
      vibrancy = 0.16,
      vibrancy_darkness = 0.0,
      noise = 0.02,
      ignore_opacity = true,
      new_optimizations = true,
    },
  },

  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})

-- Custom animations
hl.curve("overshot", { type = "bezier", points = { { 0.05, 0.9 }, { 0.1, 1.1 } } })
hl.curve("smoothOut", { type = "bezier", points = { { 0.36, 0 }, { 0.66, -0.56 } } })

hl.animation({ leaf = "windows", enabled = true, speed = 5, bezier = "overshot", style = "popin 15%" })
hl.animation({ leaf = "windowsIn", enabled = true, speed = 5, bezier = "overshot", style = "popin 15%" })
hl.animation({ leaf = "windowsOut", enabled = true, speed = 4, bezier = "smoothOut", style = "slide" })
hl.animation({ leaf = "windowsMove", enabled = true, speed = 5, bezier = "overshot" })
hl.animation({ leaf = "fade", enabled = true, speed = 4, bezier = "default" })
hl.animation({ leaf = "fadeIn", enabled = true, speed = 4, bezier = "default" })
hl.animation({ leaf = "fadeOut", enabled = true, speed = 4, bezier = "default" })
hl.animation({ leaf = "layers", enabled = true, speed = 4, bezier = "overshot", style = "popin 10%" })
hl.animation({ leaf = "layersIn", enabled = true, speed = 4, bezier = "overshot", style = "popin 10%" })
hl.animation({ leaf = "layersOut", enabled = true, speed = 3, bezier = "smoothOut", style = "slide" })
hl.animation({ leaf = "workspaces", enabled = true, speed = 6, bezier = "overshot", style = "slidefade 20%" })
