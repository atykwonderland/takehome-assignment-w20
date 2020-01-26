<template>
  <div>
    <p>{{ count }}</p>
    <button v-on:click="count ++">UP</button> 
    <button v-on:click="count --">DOWN</button>  
  </div>
</template>

<script>
export default {
  props: {
    count : Number
  },
  data() {
    return {
    };
  } 
};
</script>

<style>
</style>

