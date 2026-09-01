local active_border_color = "rgb(fab387)"
local inactive_border_color = "rgb(cba6f7)"

hl.config({
  general = {
    gaps_in = 6,
    gaps_out = 14,
    border_size = 2,
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
    resize_on_border = false,
    allow_tearing = false,
  },

  decoration = {
    rounding = 16,
    rounding_power = 2.0,

    active_opacity = 1.0,
    inactive_opacity = 0.96,
    fullscreen_opacity = 1.0,

    dim_inactive = false,

    shadow = {
      enabled = true,
      range = 30,
      render_power = 3,
      color = "rgba(00000066)",
      color_inactive = "rgba(00000033)",
      offset = "0 8",
      scale = 1.0,
    },

    blur = {
      enabled = true,
      size = 12,
      passes = 3,
      contrast = 1.0,
      brightness = 1.05,
      vibrancy = 0.18,
      vibrancy_darkness = 0.05,
      noise = 0.015,
      ignore_opacity = true,
      new_optimizations = true,
      xray = false,
    },
  },

  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
    groupbar = {
      gradients = true,
      gradient_rounding = 14,
      gradient_round_only_edges = true,
    },
  },

  animations = {
    enabled = true,
  },

  misc = {
    animate_manual_resizes = true,
    animate_mouse_windowdragging = true,
  },
})

-- Smooth, rounded-feel bezier curves
hl.curve("easeOutQuint", { type = "bezier", points = { { 0.23, 1 }, { 0.32, 1 } } })
hl.curve("easeInOutCubic", { type = "bezier", points = { { 0.65, 0 }, { 0.35, 1 } } })
hl.curve("overshot", { type = "bezier", points = { { 0.05, 0.9 }, { 0.1, 1.05 } } })
hl.curve("smoothOut", { type = "bezier", points = { { 0.36, 0 }, { 0.66, -0.56 } } })
hl.curve("smoothIn", { type = "bezier", points = { { 0.6, 0.04 }, { 0.98, 0.335 } } })

hl.animation({ leaf = "windows", enabled = true, speed = 6, bezier = "easeOutQuint", style = "slidefade 12%" })
hl.animation({ leaf = "windowsIn", enabled = true, speed = 6, bezier = "easeOutQuint", style = "slidefade 12%" })
hl.animation({ leaf = "windowsOut", enabled = true, speed = 5, bezier = "smoothOut", style = "slidefade 8%" })
hl.animation({ leaf = "windowsMove", enabled = true, speed = 5, bezier = "easeInOutCubic", style = "slide" })
hl.animation({ leaf = "border", enabled = true, speed = 8, bezier = "easeOutQuint" })
hl.animation({ leaf = "borderangle", enabled = true, speed = 12, bezier = "linear", style = "loop" })
hl.animation({ leaf = "fade", enabled = true, speed = 5, bezier = "easeOutQuint" })
hl.animation({ leaf = "fadeIn", enabled = true, speed = 5, bezier = "easeOutQuint" })
hl.animation({ leaf = "fadeOut", enabled = true, speed = 5, bezier = "smoothOut" })
hl.animation({ leaf = "workspaces", enabled = true, speed = 6, bezier = "easeOutQuint", style = "slidefade 18%" })
hl.animation({ leaf = "layers", enabled = true, speed = 5, bezier = "easeOutQuint", style = "slidefade 10%" })
hl.animation({ leaf = "layersIn", enabled = true, speed = 5, bezier = "easeOutQuint", style = "slidefade 10%" })
hl.animation({ leaf = "layersOut", enabled = true, speed = 4, bezier = "smoothOut", style = "slidefade 6%" })
