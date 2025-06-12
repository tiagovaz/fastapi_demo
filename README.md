# FastAPI Demo for SysDev Course

This project is a basic To-Do FastAPI application prepared for a System
Development course (college level). The idea is to progressively demonstrate a
basic frontend/backend/database integration, as I've seen many students having
trouble to understand the 'magic' behind a dynamic website in the beginning of
the course.

I also encourage them to perform a simple deployment in a Linux server using
systemd, uvicorn and nginx.

The idea is to start from a basic non-persistent single-file application, then
to discuss each step in order to make it persistent through a SQL database.
This codebase also helps introducing students to a few concepts such as MVC
(Model-View-Controller) and ORM (Object-Relational Mapping).

---

## Setup and run

### 1. Install Python virtual environment

```bash
sudo apt-get install python3-venv
```

### 2. Set up the project environment

```bash
cd ~/code/fastapi_demo
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi[all] requests sqlmodel
```

### 4. Enter in one of the app directories and run it with uvicorn:

```bash
uvicorn main:app --reload
```

This will start the development server with auto-reload enabled at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Running as a systemd service

To run your FastAPI app as a service using `systemd`, follow these steps:

### 1. Make the necessary changes to the services file provided and copy it to your system:

```bash
sudo cp fastapi-todo.service /etc/systemd/system/
```

### 2. Reload systemd daemon

```bash
sudo systemctl daemon-reload
```

### 3. Enable and start the service

```bash
sudo systemctl enable fastapi-todo.service
sudo systemctl start fastapi-todo.service
```

## Serving your application with Nginx

### 1. Install Nginx
```bash
sudo apt install nginx
```

### 2. Make the necessary changes to the provided Nginx config file and copy it
to /etc/nginx/sites-available/

```bash
sudo cp fastapi_todo.conf /etc/nginx/sites-available/
```

### 3. Create a link in 'sites-enabled' to enable your config:

```bash
sudo ln -s /etc/nginx/sites-available/fastapi_todo.conf /etc/nginx/sites-enabled/
```

### 4. Test and reload Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Using MariaDB (MySQL):

If you wish to use MariaDB rather than SQLite, check the following
instructions.

### 1. Install MariaDB server:

```bash
sudo apt install mariadb-server
```

### 2. Use the local client to create the database and credentials:

```bash
sudo mysql -u root
```

Then in your mariadb prompt:

```bash
CREATE DATABASE tododb;
CREATE USER 'todouser'@'localhost' IDENTIFIED BY 'yourpasswd';
GRANT ALL PRIVILEGES ON tododb.* TO 'todouser'@'localhost';
FLUSH PRIVILEGES;
```

### 3. Edit your .env accordingly:

```bash
# MySQL database URL
DATABASE_URL=mysql+pymysql://todouser:yourpasswd@localhost/tododb
```

---

## Project Structure

```
fastapi_demo/
├── 01-single-file-API (REST/JSON API)
├── 02-single-file-HTML (HTML Template Rendering)
├── 03-single-file-HTML-persistent (HTML Template Rendering, with SQL)
├── 04-MVC-HTML-persistent (HTML Template Rendering, with SQL in a modular structure - MVC)
└── resources (config for systemd, nginx, diagrams, etc)
```

Make sure your `main.py` contains the FastAPI app under the variable `app`, as expected by Uvicorn.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)
- [Nginx Docs](https://nginx.org/en/docs/)

## Next steps

- Add options to delete and update TodoItem objects
- Add one-to-many and many-to-many relationships in the TodoItem class, for example adding user and tags
- Use another DBSM such as MySQL and PostgreSQL
- Host your application in a public VPS (with a public IP address) and set a
  domain name to it
- Use certbot to create a SSL certificate from Let's Encrypt and serve your application
  through HTTPS
- Implement a basic auto-deployment using webhooks, github actions, or just a
  simple cronjob task
- Implement a backup strategy and secure your server

---

## License

This project is licensed under the MIT License.
