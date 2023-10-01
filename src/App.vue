<template>
  <img :class="{ background: true, active: active }" src="./assets/background.webp" />
  <div class="cover"></div>
  <main class="main-container">
    <DiaryBox class="diary-box"></DiaryBox>
    <AddDiary class="add-diary"></AddDiary>
    <DiaryOverview class="diary-overview"></DiaryOverview>
  </main>
</template>
<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');

h1 {
  opacity: 0.8;
  font-weight: 500;
  transition: 200ms;

  &::after {
    content: "";
    position: absolute;
    background-color: #ffffff6b;
    border-radius: 10px;
    width: 0%;
    height: 1px;
    top: 1.5em;
    transform: translateX(50%);
    transition: 200ms;
  }

  &::before {
    content: "";
    position: absolute;
    background-color: #ffffff6b;
    border-radius: 10px;
    width: 0%;
    height: 1px;
    top: 1.5em;
    transform: translateX(-150%);
    transition: 200ms;
  }

  &:hover {
    opacity: 1;
    &::after {
      content: "";
      position: absolute;
      background-color: #ffffff6b;
      border-radius: 10px;
      width: 7%;
      height: 1px;
      top: 1.5em;
      transform: translateX(50%);
    }

    &::before {
      content: "";
      position: absolute;
      background-color: #ffffff6b;
      border-radius: 10px;
      width: 7%;
      height: 1px;
      top: 1.5em;
      transform: translateX(-150%);
    }
  }
}

.main-container {
  display: grid;
  // width: 100%;
  position: fixed;
  top: 5%;
  bottom: 5%;
  left: 12%;
  right: 12%;
}

.diary-box {
  grid-column: 1 / span 2;
  grid-row: 1 / span 9;
}

.add-diary {
  grid-column: 3 / span 1;
  grid-row: 1 / span 1;
}

.diary-overview {
  grid-column: 3 / span 1;
  grid-row: 2 / span 8;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  font-family: -apple-system, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", 'Inter', "Helvetica Neue", sans-serif;
  user-select: none;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.cover {
  z-index: -1;
  opacity: 1;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(rgba(0, 0, 0, 0) 0, rgba(0, 0, 0, .5) 100%), radial-gradient(rgba(0, 0, 0, 0) 33%, rgba(0, 0, 0, .3) 166%);
  transition: .25s;
  background-color: rgba(0, 0, 0, .1);
}

.background {
  opacity: 1;
  z-index: -3;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 1s, transform .25s, filter .25s;
  backface-visibility: hidden;

  &:is(.active) {
    transform: scale(1.1);
    filter: blur(10px);
  }
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.2s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
<script lang="ts">
import { defineComponent } from 'vue';
import AddDiary from './components/AddDiary.vue';
import DiaryBox from './components/DiaryBox.vue';
import DiaryOverview from './components/DiaryOverview.vue';
export default defineComponent({
  components: { DiaryBox, AddDiary, DiaryOverview },
  data() {
    return {
      active: false,
    }
  },
  methods: {

  }
});
</script>