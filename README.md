🛍️ E-commerce Web App (Dockerized)

A fully functional E-commerce website built using HTML, CSS, JavaScript, and Python with features like authentication, shopping cart, product filtering, pagination, and security. The project is Dockerized for easy deployment and scalability.


---

🚀 Features

✅ User Authentication – Secure login, signup, and password reset.
✅ Shopping Cart – Add, update, and remove items.
✅ Product Management – Display products with categories and filters.
✅ Related Products – Smart product suggestions.
✅ Pagination – Load more products dynamically.
✅ Secure Checkout – MPesa or other payment gateways.
✅ Order Tracking – View order history and statuses.
✅ Admin Panel – Manage products, users, and orders.
✅ SEO Optimized – Fast-loading and mobile-friendly.
✅ Fully Responsive – Works on all screen sizes.
✅ Dockerized – Run the app using Docker for easy deployment.


---

📦 Tech Stack


---

📂 Project Structure

📦 ecommerce-web
├── 📁 static               
│   ├── styles.css         
│   ├── scripts.js         
├── 📁 templates            
│   ├── index.html         
│   ├── product.html       
│   ├── cart.html         
│   ├── checkout.html      
│   ├── login.html         
├── 📁 backend        
│   ├── manage.py          
│   ├── database.py       
│   ├── auth.py           
│   ├── cart.py           
├── 📁 docker             
│   ├── Dockerfile       
│   ├── docker-compose.yml 
├── .env                   
├── requirements.txt       
├── manage.py              
└── README.md      


---

🛠️ Installation

Prerequisites

Docker & Docker Compose installed

Git installed


1️⃣ Clone the repository

git clone https://github.com/D3ras/smartpoolers.git

cd smartpoolers

2️⃣ Set up environment variables

Create a .env file in the root directory:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
MPESA_KEY=your-mpesa-key

3️⃣ Build and run the application

docker-compose up --build

4️⃣ Open in your browser

Frontend: http://localhost:8000

Admin Panel: http://localhost:8000/admin



---

🔒 Security Features

Secure Authentication with hashed passwords

CSRF Protection for secure forms

Rate Limiting to prevent abuse

SSL Ready for encrypted connections



---

📖 API Endpoints (if applicable)


---

📦 Deployment

For production, use:

docker-compose -f docker-compose.prod.yml up --build -d

Nginx handles static files and reverse proxy.

Gunicorn manages backend requests.

Let's Encrypt SSL for HTTPS.



---

🚀 Future Enhancements

AI-powered recommendations (LLM + FAISS).

Multi-vendor support for multiple sellers.

GraphQL API for better frontend performance.

Progressive Web App (PWA) for mobile experience.



---

🤝 Contributing

1. Fork the project


2. Create a feature branch (git checkout -b feature-name)


3. Commit changes (git commit -m "Added new feature")


4. Push to the branch (git push origin feature-name)


5. Open a pull request




---

📜 License

This project is licensed under the MIT License.


---

📧 Contact

Company: 

Website: 

Email: peternjengaderas@gmail.com

