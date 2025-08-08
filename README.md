# Flask Frontend Compendium

This is a learning-focused Flask-based project designed to explore and demonstrate frontend skills (HTML, CSS, JS) in a practical and organized way.
The project is containerized using Docker for easy development and deployment.

---

## Features

- Dockerized Flask environment
- Static frontend examples (HTML/CSS/JS)
- Modular structure for frontend topics
- Markdown-based articles and tutorials
- Simple endpoints for demo purposes

---

## How to Start Project

### 1. Clone the repository

```bash
git clone https://github.com/Paradox60/flask-front-end.git
cd flask-front-end
```

### 2. Create `.env` file

```bash
cp .env.example .env
```
Change variables if needed

### 3. Run with Docker

```bash
docker-compose up --build
```

The app will be available at [http://localhost:5000](http://localhost:5000)

---

## 🧠 Purpose

This project is intended for:

- Practicing and showcasing frontend skills within a Flask context
- Creating small interactive components (e.g. dropdowns, sliders, modals)
- Writing Markdown-based frontend guides and tutorials
- Learning project organization and deployment basics

---

## 📚 Articles & Demos

Articles are stored in the `content/` directory and rendered dynamically as HTML pages.
New topics can be added easily as Markdown files.

---

## TODO

- [ ] Add markdown rendering
- [ ] Add syntax highlighting
- [ ] Add examples for forms, JS interactivity
- [ ] Add dark mode
- [ ] Add simple REST API
- [ ] Improve layout with modern CSS (Flexbox, Grid, etc.)
- [ ] Integrate basic JavaScript interactions (DOM, events)


---

## License

This project is open for learning purposes.
Feel free to fork and build upon it!
