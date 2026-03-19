# Slides (Marp)

This folder contains the Week 1 sandbox slide deck source.

## File

- [week1-sandbox-deck.md](week1-sandbox-deck.md)

## Present in VS Code

1. Install **Marp for VS Code** (`marp-team.marp-vscode`)
2. Open [week1-sandbox-deck.md](week1-sandbox-deck.md)
3. Open Marp preview (`Marp: Open Preview`)

## Export

From Marp preview, export as PDF or PowerPoint.

Optional CLI export:

```bash
npx @marp-team/marp-cli slides/week1-sandbox-deck.md --pdf --output slides/week1-sandbox-deck.pdf
```

## Add Images

Yes — Marp supports images directly in markdown.

Recommended location:
- `slides/assets/`

Basic image syntax:

```markdown
![Trip prompt example](assets/trip-prompt-example.png)
```

Resize image in slide:

```markdown
![w:900](assets/trip-prompt-example.png)
```

Center an image on a slide:

```markdown
![bg contain](assets/trip-prompt-example.png)
```

Tips:
- Prefer `.png` for screenshots and `.jpg` for photos.
- Keep file names lowercase with hyphens.
- Use relative paths from the slide file (`assets/...`).

## Example SVG Assets

- [assets/think-pair-share.svg](assets/think-pair-share.svg)
- [assets/bridge-to-week2.svg](assets/bridge-to-week2.svg)
- [assets/exit-ticket.svg](assets/exit-ticket.svg)
