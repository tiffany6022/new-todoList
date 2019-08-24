<template lang="pug">
#app

  #input.ui.input.action
    input(type="text", v-model='todo', placeholder="add todo..." @keydown.enter='addTask()')
    button.ui.icon.button(@click='addTask()')
      i.plus.icon

  .task(v-for="task in tasks")
    .ui.checkbox(@click='toggleTask(task)')
      input(type="checkbox" v-model='task.toggle')
      label(v-if='!task.toggle') {{task.name}}
      label(v-if='task.toggle')
        del {{task.name}}
    i.delete.icon(v-if='task.toggle' @click='rmTask(task)')
    task-detail(:detail="task.detail")

</template>

<script>
const axios = require('axios')

export default {

  components: {
    'task-detail': require('./AppDetail.vue').default
  },

  created() {
    axios.get('/c')
    .then((res)=>{
       console.log(res)
    })
  },

  data() {return {
    todo: 'Data binding is cool!',
    tasks: []
  }},

  methods: {

    addTask(){
      if (!this.todo)
        return
      let task = {
        name: this.todo,
        detail: 'aaaa',
        toggle: false
      }

      this.tasks.push(task)
      axios.get('/add', {params: task})
      .then((res)=>{
        console.log(res)
      })
      this.todo = ''
    },

    rmTask(tsk) {
      this.tasks = this.tasks.filter(task => task != tsk)
    },

    toggleTask(tsk) {
      const toggle = this.tasks.find(task => task === tsk).toggle
      this.tasks.find(task => task === tsk).toggle = !toggle

    }
  }
}
</script>

<style lang="sass">
html
  font-size: large
#app
  width: 22em
  margin: auto
  display: flex
  flex-direction: column
  padding: 2em
.task
  margin-top: 1em
  display: flex
  justify-content: space-between
</style>
