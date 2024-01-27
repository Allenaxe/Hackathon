<template>
    <div class="signup-container">
    <div class="signup-form">
      <h1>Sign Up</h1>
      <p class="subtitle">Sign up to enjoy your learning trip</p>
      <form @submit.prevent="submitForm">
        <p class="smalltitle">Choose a picture to be your profile pic</p>
        <div id="img-preview" v-if="imageData">
          <img :src="imageData" alt="Profile Preview">
        </div>
        <input type="file" id="choose-file" @change="previewImage" accept="image/*" />
        <div class="form-group">
          <label for="name">Username</label>
          <el-input class="input"  id="name" v-model="formInline.username" placeholder="User name"></el-input>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <el-input class="input" id="email" v-model="formInline.email" placeholder="Email"></el-input>
        </div>
        <div class="form-group">
          <label for="age">Age</label>
          <el-input class="input"  id="age" v-model="formInline.age" placeholder="Age"></el-input>
        </div>
        <div class="form-group">
          <label for="department">Department</label>
          <el-input class="input" id= "department" v-model="formInline.department" placeholder="Department"></el-input>
        </div>
        <div class="form-group">
          <label for="skills">Skills</label>
          <el-select
            v-model="formInline.skills"
            multiple
            collapse-tags
            placeholder="Select your skills">
            <el-option
              v-for="skill in skillsList"
              :key="skill.value"
              :label="skill.label"
              :value="skill.value">
            </el-option>
          </el-select>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id ="password" v-model="formInline.password" placeholder="Password" required @input="validatePassword">
          <ul class="password-requirements">
            <li v-if="!passwordValidation.minLength">Least 6 characters</li>
            <li v-if="!passwordValidation.numberOrSymbol">Least one number (0-9) or a symbol</li>
          </ul>
        </div>
        <el-button type="primary" native-type="submit">Sign Up</el-button>
      </form>
      <!-- <el-form-item>
        <el-button type="primary" @click="onSubmitGet">Get Query All</el-button>
        <el-button type="primary" @click="onSubmitPost">Post Submit</el-button>
      </el-form-item>
      <el-input type="textarea" :rows="6" placeholder="Results here" v-model="results" class="textarea"></el-input> -->
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      formInline: {
        username: '',
        email: '',
        age: '',
        department: '',
        password: '',
        skills:[],
      },
      skillsList: [
        { value: 'html', label: 'HTML' },
        { value: 'css', label: 'CSS' },
        { value: 'javascript', label: 'JavaScript' },
        { value: 'statistical Analysis', label: 'Statistical Analysis' },
        { value: 'engineering', label: 'Engineering' },
        { value: 'marketing', label: 'Marketing' },
        { value: 'political science', label: 'Political science' },
        { value: 'biochemistry', label: 'Biochemistry' },
        { value: 'psychology', label: 'Psychology' },
        { value: 'programming', label: 'Programming' },
        { value: 'art', label: 'Art' },
        { value: 'psychology', label: 'Psychology' },
        { value: 'machine Learning', label: 'Machine Learning' },
        { value: 'english', label: 'English' },
        { value: 'finance', label: 'Finance' },
        { value: 'python', label: 'Python' },
        { value: 'astronomy', label: 'Astronomy' },
        { value: 'management', label: 'Management' },
        { value: 'cloud Computing', label: 'Cloud Computing' },
        { value: 'ecology', label: 'Ecology' },
        { value: 'python', label: 'Python' },
        { value: 'geology', label: 'Geology' },
        { value: 'java', label: 'Java' },
        { value: 'philosophy', label: 'Philosophy' },
        { value: 'music', label: 'Music' },
        { value: 'unix', label: 'Unix' },
        { value: 'c', label: 'C' },
        { value: 'c++', label: 'C++' },
        
        // ... more skills ...
      ],
      passwordValidation: {
        minLength: true,
        numberOrSymbol: true,
      },
      results: '',
      imageData: null, // make sure you have imageData defined if you're using previewImage method
    };
  },
  methods: {
    validatePassword() {
      // Directly reference the password from formInline
      const password = this.formInline.password;
      this.passwordValidation.minLength = password.length >= 6;
      this.passwordValidation.numberOrSymbol = /[0-9]|[\W_]/.test(password);
    },
    
    onSubmitGet() {
      console.log('submit! get');
      axios.get('http://127.0.0.1:8000/users/', this.formInline)
        .then(res => {
          this.results = JSON.stringify(res.data);
          console.log(res.data);
        })
        .catch(error => {
          console.error('Error:', error);
          alert('An error occurred');
        });
    },
    onSubmitPost() {
      console.log('submit! post');
      axios.post('http://127.0.0.1:8000/users/', this.formInline)
        .then(res => {
          this.results = JSON.stringify(res.data);
          console.log(res.data);
        })
        .catch(error => {
          console.error('Error:', error);
          alert('An error occurred');
        });
    },
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    previewImage(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = e => {
          this.imageData = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
  },
};
</script>

<style scoped>

.signup-container {
  background: url('../images.jpg')  center center fixed;
  background-size: cover;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
}

.signup-form {
  background: rgba(0, 0, 0, 0.1);
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  color: #333;
  margin-bottom: 0.5rem;
}

.form-group input, .form-group select {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* Style the button */
.el-button--primary {
  width: 100%;
  padding: 0.5rem;
  border: none;
  border-radius: 4px;
  background-color: darkgreen;
  color: white;
  cursor: pointer;
}
.signup-form h1{
  color: white;
}
.signup-form .subtitle{
  color:lightgray;

}
.signup-form label{
  color:rgb(189, 193, 231)
}
.el-button--primary:hover {
  background-color: transparent;
}
/* Style for image preview */
.image-preview {
  margin-bottom: 1rem;
}

.image-preview img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}

.file-input-label {
  display: inline-block;
  background-color: #fff;
  color: #007bff;
  padding: 10px 15px;
  border-radius: 5px;
  margin-top: 10px;
  border: 1px solid #ccc;
  cursor: pointer;
}

button {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
