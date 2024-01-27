<template>
    <div class="login-container">
      <div class="circle bottom-left"></div> <!-- Large circle in the bottom left corner -->
      <div class="circle top-right"></div>   <!-- Small circle in the top right corner -->
      <div class="login-form">
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
          <div class="input-container">
            <input type="email" v-model="loginData.email" placeholder="Email ID" required>
          </div>
          <div class="input-container">
            <input type="password" v-model="loginData.password" placeholder="Password" required>
          </div>
          <button type="submit">Login</button>
          <div class="links">
            <!-- The `router-link` component is fine as it is, for declarative navigation -->
            <router-link to="register">Create new account</router-link>
          </div>
        </form>
      </div>
    </div>
  </template>  
  
  <script>
  export default {
    data() {
      return {
        loginData: {
          email: '',
          password: ''
        }
      };
    },
    methods: {
      submitForm() {
        // Handle the login logic here, e.g., validating the user credentials
        console.log('Login data', this.loginData);
  
        // Programmatically navigate to a new route on successful login
        // Assuming you want to navigate to '/home'
        this.$router.push('/register');
      }
    }
  };
  </script>
<style scoped>
  .login-container {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
  overflow: hidden; 
}

.circle {
  position: absolute;
  border-radius: 50%;
  background-color: #56c14a; /* Adjust the color to match your design */
}

.bottom-left {
  width: 650px; /* Large circle size */
  height: 600px; /* Large circle size */
  bottom: -30%; 
  left: -30%; 
}

.top-right {
  width: 300px; /* Small circle size */
  height: 250px; /* Small circle size */
  top: -10%; 
  right: -10%; 
}

.login-form {
  z-index: 10;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  width:250px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: relative; /* This ensures that the form is above the circles */
}
  
  h1 {
    margin-bottom: 2rem;
    text-align: center;
  }
  
  .input-container {
    margin-bottom: 1rem;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 0.5rem;
    border: none;
    border-radius: 4px;
    background-color: rgb(103, 214, 186);
    color: white;
    cursor: pointer;
  }
  
  button:hover {
    background-color: forestgreen;
  }
  
  .links {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1rem;
  }
  
  .links a {
    color: #007bff;
    text-decoration: none;
  }
  
  .links span {
    padding: 0 0.5rem;
  }
  </style>
  