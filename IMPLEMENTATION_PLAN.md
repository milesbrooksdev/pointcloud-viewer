# PointCloud Viewer Implementation Plan
## Date: 2026-02-19

## Overview
Update 4 LUMO pages to match index.html's green/cyberpunk theme, update index.html cursor to match the enhanced cursor from the 4 pages, and fix navigation across all pages.

---

## Phase 1: Update index.html Cursor (index.html)

### 1.1 Update CSS Cursor Styles

**Current cursor-outline CSS (lines ~295-310):**
```css
.cursor-outline {
    position: fixed;
    top: 0; left: 0; width: 40px; height: 40px;
    border: 1px solid rgba(0, 255, 106, 0.4);
    border-radius: 50%;
    z-index: 9999;
    pointer-events: none;
    transform: translate(-50%, -50%);
    transition: width 0.2s, height 0.2s;
    mix-blend-mode: screen;
}
```

**Change to:**
```css
.cursor-outline {
    position: fixed;
    top: 0; left: 0; width: 40px; height: 40px;
    border: 1px solid rgba(0, 255, 106, 0.4);
    border-radius: 50%;
    z-index: 9999;
    pointer-events: none;
    transform: translate(-50%, -50%);
    transition: width 0.2s, height 0.2s;
    mix-blend-mode: color-burn;
}

.cursor-outline::before, .cursor-outline::after {
    content: ''; 
    position: absolute; 
    background: var(--c-accent);
}
.cursor-outline::before { 
    top: 50%; 
    left: -20%; 
    right: -20%; 
    height: 1px; 
}
.cursor-outline::after { 
    left: 50%; 
    top: -20%; 
    bottom: -20%; 
    width: 1px; 
}
```

### 1.2 Update JavaScript Cursor Animation

**Current ease value (in animateCursor function):**
```javascript
const ease = 0.1;
```

**Change to:**
```javascript
const ease = 0.15;
```

### 1.3 Update Hover Effects

**Current hover handlers (end of script):**
```javascript
document.querySelectorAll('.btn, .nav-text').forEach(btn => {
    btn.addEventListener('mouseenter', () => {
        cursorOutline.style.width = '60px';
        cursorOutline.style.height = '60px';
        cursorOutline.style.borderColor = '#00ff6a';
    });
    btn.addEventListener('mouseleave', () => {
        cursorOutline.style.width = '40px';
        cursorOutline.style.height = '40px';
        cursorOutline.style.borderColor = 'rgba(0, 255, 106, 0.4)';
    });
});
```

**Change to:**
```javascript
document.querySelectorAll('.btn, .nav-text, .brand').forEach(el => {
    el.addEventListener('mouseenter', () => {
        cursorOutline.style.width = '70px';
        cursorOutline.style.height = '70px';
        cursorOutline.style.borderColor = '#00ff6a';
        cursorOutline.style.backgroundColor = 'rgba(0, 255, 106, 0.05)';
    });
    el.addEventListener('mouseleave', () => {
        cursorOutline.style.width = '40px';
        cursorOutline.style.height = '40px';
        cursorOutline.style.borderColor = 'rgba(0, 255, 106, 0.4)';
        cursorOutline.style.backgroundColor = 'transparent';
    });
});
```

### 1.4 Update Navigation Links

**Current header nav (lines ~210-220):**
```html
<header class="header-top">
    <a href="#" class="nav-text brand">C4 Studios</a>
    <div style="display: flex; gap: 3rem;">
        <a href="#" class="nav-text">Projects</a>
        <a href="#" class="nav-text">Capabilities</a>
    </div>
</header>
```

**Change to:**
```html
<header class="header-top">
    <a href="index.html" class="nav-text brand">LUMO Studios</a>
    <div style="display: flex; gap: 3rem;">
        <a href="LumoCuratedArchive.html" class="nav-text">Projects</a>
        <a href="LumoCapabilitites.html" class="nav-text">Capabilities</a>
        <a href="LumoNaritave.html" class="nav-text">About</a>
    </div>
</header>
```

Also update brand name throughout the page (hero text, coords, etc.):
- Change "C4 Studios" to "LUMO Studios"
- Change "C4 STUDIOS" to "LUMO STUDIOS"

---

## Phase 2: Update LumoCapabilitites.html

### 2.1 Update :root CSS Variables

**Current:**
```css
:root {
    --c-bg-base: #fdf2e9;
    --c-bg-overlay: rgba(230, 126, 34, 0.05);
    --c-text-main: #4a2c2a;
    --c-text-muted: #8e6d6b;
    --c-accent: #e67e22;
    --c-secondary-accent: #ff7f50;
    --c-golden: #f39c12;
    ...
}
```

**Change to:**
```css
:root {
    --c-bg-base: #0a0f0a;
    --c-bg-overlay: rgba(0, 255, 100, 0.03);
    --c-text-main: #b8ffcc;
    --c-text-muted: #5a8f6a;
    --c-accent: #00ff6a;
    --c-secondary-accent: #39ff85;
    --c-golden: #00c94a;
    ...
}
```

### 2.2 Update Three.js Scene Background

**Current (in module script):**
```javascript
scene.background = new THREE.Color(0xfdf2e9);
```

**Change to:**
```javascript
scene.background = new THREE.Color(0x0a0f0a);
```

### 2.3 Update Particle Colors

**Current:**
```javascript
const color = new THREE.Color(0xe67e22);
```

**Change to:**
```javascript
const color = new THREE.Color(0x00ff6a);
```

### 2.4 Update Cursor Outline Mix Blend Mode

**Current:**
```css
mix-blend-mode: color-burn;
```

**Change to:**
```css
mix-blend-mode: screen;
```

### 2.5 Update Cursor Hover Colors

**Current:**
```javascript
cursorOutline.style.borderColor = '#e67e22';
// and
cursorOutline.style.borderColor = 'rgba(230, 126, 34, 0.4)';
```

**Change to:**
```javascript
cursorOutline.style.borderColor = '#00ff6a';
// and
cursorOutline.style.borderColor = 'rgba(0, 255, 106, 0.4)';
```

### 2.6 Update Border Colors Throughout

**Current:**
```css
border-bottom: 1px solid rgba(142, 109, 107, 0.2);
```

**Change to:**
```css
border-bottom: 1px solid rgba(0, 255, 106, 0.15);
```

**Current:**
```css
border: 1px solid rgba(142, 109, 107, 0.3);
```

**Change to:**
```css
border: 1px solid rgba(0, 255, 106, 0.25);
```

### 2.7 Update Navigation Links

**Current:**
```html
<a href="index.html" class="nav-text brand">LUMO studios</a>
<div style="display: flex; gap: 3rem;">
    <a href="#" class="nav-text">Projects</a>
    <a href="#" class="nav-text active">Capabilities</a>
</div>
```

**Change to:**
```html
<a href="index.html" class="nav-text brand">LUMO Studios</a>
<div style="display: flex; gap: 3rem;">
    <a href="LumoCuratedArchive.html" class="nav-text">Projects</a>
    <a href="LumoCapabilitites.html" class="nav-text active">Capabilities</a>
    <a href="LumoNaritave.html" class="nav-text">About</a>
</div>
```

---

## Phase 3: Update LumoCuratedArchive.html

### 3.1 Update :root CSS Variables

**Change from warm to green theme (same as Phase 2.1)**

### 3.2 Update Hardcoded Colors

**Current (in inline style):**
```html
<a href="#" class="nav-text" style="color: var(--c-accent)">Projects</a>
```

This will auto-update with CSS variable change.

**Current (project-image-wrapper):**
```css
background-color: rgba(230, 126, 34, 0.1);
```

**Change to:**
```css
background-color: rgba(0, 255, 106, 0.1);
```

**Current (project-overlay):**
```css
background: rgba(74, 44, 42, 0.4);
```

**Change to:**
```css
background: rgba(10, 15, 10, 0.4);
```

**Current (footer-logo):**
```css
color: rgba(74, 44, 42, 0.1);
```

**Change to:**
```css
color: rgba(184, 255, 204, 0.1);
```

### 3.3 Update Cursor Hover Effects

**Current:**
```javascript
cursorOutline.style.backgroundColor = 'rgba(230, 126, 34, 0.05)';
```

**Change to:**
```javascript
cursorOutline.style.backgroundColor = 'rgba(0, 255, 106, 0.05)';
```

### 3.4 Update Cursor Mix Blend Mode

**Change from:**
```css
mix-blend-mode: color-burn;
```

**To:**
```css
mix-blend-mode: screen;
```

### 3.5 Update Border Colors

Same pattern as Phase 2.5-2.6

### 3.6 Update Navigation Links

**Current:**
```html
<a href="index.html" class="nav-text brand">LUMO studios</a>
<div style="display: flex; gap: 3rem;">
    <a href="#" class="nav-text" style="color: var(--c-accent)">Projects</a>
    <a href="#" class="nav-text">Capabilities</a>
</div>
```

**Change to:**
```html
<a href="index.html" class="nav-text brand">LUMO Studios</a>
<div style="display: flex; gap: 3rem;">
    <a href="LumoCuratedArchive.html" class="nav-text" style="color: var(--c-accent)">Projects</a>
    <a href="LumoCapabilitites.html" class="nav-text">Capabilities</a>
    <a href="LumoNaritave.html" class="nav-text">About</a>
</div>
```

---

## Phase 4: Update LumoLoadingScreen.html

### 4.1 Update :root CSS Variables

**Current includes:**
```css
--c-skeleton: #f3e5d8;
```

**Change to:**
```css
--c-skeleton: #1a2a1a;
```

And update all other color variables as in Phase 2.1.

### 4.2 Update Skeleton Sphere Styles

**Current:**
```css
background: radial-gradient(circle, var(--c-skeleton) 0%, transparent 70%);
border: 1px dashed rgba(230, 126, 34, 0.15);
```

**Change to:**
```css
background: radial-gradient(circle, var(--c-skeleton) 0%, transparent 70%);
border: 1px dashed rgba(0, 255, 106, 0.15);
```

**Current:**
```css
background: linear-gradient(90deg, transparent, rgba(230, 126, 34, 0.2), transparent);
```

**Change to:**
```css
background: linear-gradient(90deg, transparent, rgba(0, 255, 106, 0.2), transparent);
```

### 4.3 Update Loading Bar

**Current:**
```css
background: rgba(230, 126, 34, 0.2);
```

**Change to:**
```css
background: rgba(0, 255, 106, 0.2);
```

### 4.4 Update Cursor Styles

Same as Phase 2.4-2.5

### 4.5 Update Navigation Links

Same as Phase 3.6 (but without the inline style on Projects since this is the loading screen concept)

---

## Phase 5: Update LumoNaritave.html

### 5.1 Update :root CSS Variables

Same as Phase 2.1

### 5.2 Update Hardcoded Colors

**Current (inline style):**
```html
<a href="#" class="nav-text" style="color: var(--c-accent);">About</a>
```

This will auto-update.

**Current (timeline-container border):**
```css
border-left: 1px solid rgba(230, 126, 34, 0.2);
```

**Change to:**
```css
border-left: 1px solid rgba(0, 255, 106, 0.15);
```

**Current (timeline-item::before):**
```css
background: var(--c-accent);  /* this will auto-update */
```

**Current (team-image-container):**
```css
background: #e8ded4;
```

**Change to:**
```css
background: #1a2a1a;
```

### 5.3 Update Cursor Hover Background

**Current:**
```javascript
cursorOutline.style.background = 'rgba(230, 126, 34, 0.05)';
```

**Change to:**
```javascript
cursorOutline.style.background = 'rgba(0, 255, 106, 0.05)';
```

### 5.4 Update Navigation Links

**Current:**
```html
<a href="/" class="brand">LUMO studios</a>
<nav style="display: flex; gap: 3rem;">
    <a href="#" class="nav-text">Projects</a>
    <a href="#" class="nav-text" style="color: var(--c-accent);">About</a>
    <a href="#" class="nav-text">Capabilities</a>
</nav>
```

**Change to:**
```html
<a href="index.html" class="brand">LUMO Studios</a>
<nav style="display: flex; gap: 3rem;">
    <a href="LumoCuratedArchive.html" class="nav-text">Projects</a>
    <a href="LumoNaritave.html" class="nav-text" style="color: var(--c-accent);">About</a>
    <a href="LumoCapabilitites.html" class="nav-text">Capabilities</a>
</nav>
```

---

## Summary of Color Mappings

| Warm Theme (Old) | Green Theme (New) |
|-----------------|-------------------|
| #fdf2e9 (cream bg) | #0a0f0a (dark green-black) |
| #4a2c2a (dark brown text) | #b8ffcc (light green text) |
| #8e6d6b (muted brown) | #5a8f6a (muted green) |
| #e67e22 (orange accent) | #00ff6a (bright green) |
| #ff7f50 (coral) | #39ff85 (light green) |
| #f39c12 (golden) | #00c94a (green-gold) |
| #f3e5d8 / #e8ded4 (skeleton) | #1a2a1a (dark green) |
| rgba(230, 126, 34, x) | rgba(0, 255, 106, x) |
| rgba(142, 109, 107, x) | rgba(0, 255, 106, x) |
| rgba(74, 44, 42, x) | rgba(10, 15, 10, x) |

---

## Testing Checklist

- [ ] All pages have consistent green/cyberpunk color scheme
- [ ] All pages have working navigation links to each other
- [ ] Cursor has smooth trailing animation (ease: 0.15)
- [ ] Cursor has crosshair lines (::before/::after)
- [ ] Cursor expands and shows background fill on hover
- [ ] Three.js scenes have dark background and green particles
- [ ] All borders use green accent colors
- [ ] Text is readable with good contrast


## 2026-02-19 Update — C4 Light Teal Palette Rollout

Applied the palette defined in `colorPalleteC4.html` across working pages:

- `index.html`
- `projects.html` (Selected Work)
- `c4-curated-archive.html`
- `c4-capabilities.html`
- `c4-about.html`
- `c4-loading.html`

### Canonical Color Tokens
- `--c-bg-base: #f0f7f9`
- `--c-bg-overlay: rgba(0, 128, 128, 0.05)`
- `--c-text-main: #0a192f`
- `--c-text-muted: #4a6fa5`
- `--c-accent: #008080`
- `--c-secondary-accent: #00a8a8`
- `--c-golden: #00ced1`

### Additional Normalization
- Updated hardcoded green glow/border values to teal/cyan equivalents.
- Updated Three.js accent/light colors to align with the new palette where used.
- Kept navigation structure synchronized (Selected Work + Curated Archive + Capabilities + About).
