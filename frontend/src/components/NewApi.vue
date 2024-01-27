<template>
  <div id="rRRecord">
    <div class="level-system">
      <div class="stars">
        <img v-if="stars === 0" src="../download1.jpg" class="star" />
        <img v-for="n in getstar()" :key="n" src="../download.jpg" class="star" />
      </div>
      <button @click="addStar">Add Star</button>
      <div class="word">Level: {{ level }}</div>
    </div>
    <div class="badge-section">
      <h2 class="badge-title">
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        Highlights Badges
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
        <span class="badge-title-decor">✨</span>
      </h2>
      <table class="badge-table">
        <tbody>
          <tr v-for="(badge, index) in badges" :key="badge.name" class="badge-row">
            <td class="badge-icon-cell">
              <img v-if="shouldShowArrow(index)" src="../arrow.png" class="arrow-icon"/>
            <img :src="badge.icon" :alt="badge.name" class="badge-icon"/></td>
            <td class="badge-name">{{ badge.name }}</td>
            <td class="badge-how-to-get">{{ badge.howToGet }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import badge1  from '../badge1.jpg';
import badge2  from '../badge2.jpg';
import badge3  from '../badge3.jpg';
import badge4  from '../badge4.png';
import badge5  from '../badge5.jpg';
import axios from 'axios';
export 
default {
  name: 'rRRecord',
  data() {
    return {
      stars: 0,
      level: 1,
      badges: [
        { icon:badge1, name: 'Elementary', howToGet: 'Good!!!' },
        { icon:badge2,name: 'Moderate', howToGet: 'Keep learning fighter !' },
        { icon:badge3,name: 'Adcanced', howToGet: 'You have win over half of the learners.' },
        { icon:badge4,name: 'Professor', howToGet: 'Congratulations !' },
        { icon:badge5,name: 'The best of the community', howToGet: 'You are Einstein.' },
      ],
      results: 0
    };
  },
  methods: {
    shouldShowArrow(index) {
      return (index === 0 && this.level <= 5) || (index === 1 && this.level > 5 && this.level <= 10) ||(index === 2 && this.level > 10 && this.level <= 15) ||(index === 3 && this.level > 15 && this.level <= 20 ) ||(index === 3 && this.level > 20 && this.level <= 25 );
    },
    async getstar() {
      await axios.get('http://127.0.0.1:8000/students/printUser')
      .then(res => {
          this.results = res.data.Score;
          console.log(res.data.Score);
        })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
      });
      return this.results;
    },
    addStar() {
      if (this.stars < 4) {
        this.stars += 1;
      } else {
        this.stars = 0;
        this.level += 1;
      }
    }
  }
}
</script>

<style>
/* Add global styles here */
.level-system{
  color: #fff;
  background-color: #222322;
  padding: 0.3em;
  /* Style your star image */
}

.badge-section {
  color: #fff;
  background-color: rgb(39, 41, 40)  ;
  padding: 1em;
  border-radius: 1px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.badge-title {
  text-align: center;
  font-size: 1.5em;
  color: #FFC107;
  margin-bottom: 1em;
}
.badge-title-decor {
  display: inline-block;
  margin: 0 0.5em;
}
.badge-table {
  width: 100%;
  border-collapse: collapse;
}
.badge-row {
  border-top: 1px solid #94a7a0;
}
.badge-icon-cell {
  padding: 0.5em;
  text-align: center;
}
.badge-icon {
  width: 30px;
  height: 30px;
}
.badge-name{
  padding: 0.5em;
  font-weight: bold;
  text-align: left;
}
.badge-how-to-get {
  padding: 0.5em;
  text-align: left;

}
.word{
  text-align: center;
  font-size: 2em;
  color: #c6cdc6;
  font-weight: bold;
  margin-bottom: 1em;
}
</style>
