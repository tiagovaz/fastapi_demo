# FastAPI Demo for SysDev Course

This project is a basic FastAPI application prepared for a System Development
course (college level). The idea is to progressively demonstrate a basic
frontend/backend/database integration, as I've seen many students having
trouble to understand the 'magic' behind a dynamic website in the beginning of
the course.

I also present them a simple deployment strategy in a Linux server using
systemd, uvicorn and nginx.

The idea is to start from a basic non-persistent single-file application, then
to discuss each step in order to make it persistent through a SQL database.
This codebase also helps introducing students to a few concepts such as MVC
(Model-View-Controller) and ORM (Object-Relational Mapping).

---

## Quickstart

### 1. Install Python Virtual Environment Tools

```bash
sudo apt-get install python3-venv
```

### 2. Set Up the Project Environment

```bash
cd ~/code/fastapi_demo
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi[all] requests sqlmodel
```

### 4. Enter in one of the directories (01, 02, etc) and serve your application through uvicorn:

```bash
uvicorn main:app --reload
```

This will start the development server with auto-reload enabled at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Running as a systemd Service

To run your FastAPI app as a service using `systemd`, follow these steps:

### 1. Make the necessary changes to the services file provided and copy it to your system:

```bash
sudo cp fastapi-todo.service /etc/systemd/system/
```

### 2. Reload systemd Daemon

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

### 3. Enable and Start the Service

```bash
sudo systemctl enable fastapi-todo.service
sudo systemctl start fastapi-todo.service
```

---

## Project Structure

```
fastapi_demo/
├── 01-single-file-API (REST/JSON API)
├── 02-single-file-HTML (HTML Template Rendering)
├── 03-single-file-HTML-persistent (HTML Template Rendering, with SQL)
├── 04-MVC-HTML-persistent (HTML Template Rendering, with SQL in a modular structure - MVC)
└── Resources (systemd, nginx, diagrams, etc)
```

Make sure your `main.py` contains the FastAPI app under the variable `app`, as expected by Uvicorn.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)

---

## License

This project is licensed under the MIT License.
