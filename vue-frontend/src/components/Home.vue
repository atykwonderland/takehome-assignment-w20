<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions complete=True />
    <!-- PART 4: Modify the Show component to accept all of these props -->
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />
    <form>
      <input type="text" v-model="show" placeholder="Show Name">
      <button type="button" @click="add">
        Add a New Show
      </button>
    </form>
    </br>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ],
      show: ''
    };
  },
  methods: {
    add() {
      n = shows.length
      shows.push({ id: n, name: this.show, episodes_seen: 0 })
    }
  }
};
</script>

<style>
</style>


