<template lang="pug">
#app
  .ui.action.input
    input(type="text", v-model="todo", @keydown.enter="addTask()")
    button.ui.icon.button(@click="addTask()")
      i.plus.icon

  .ui.checkbox.task(v-for="task in tasks")
    input(type="checkbox", v-model="task.done")
    label(v-if="task.done")
      del {{ task.title }}
    label(v-else) {{ task.title }}
    i.close.icon(@click="deleteTask(task)", v-if="task.done")
</template>


<script>
  export default{
    data(){
      return{
        todo: "abc",
        tasks: []
      }
    },
    methods: {
      addTask: function(){
        var tsk = this.todo;
        if(tsk){
          this.tasks.push({
            title: tsk,
            done: false
          });
          this.todo = "";
        }
      },
      deleteTask: function(tsk){
        this.tasks.splice(this.tasks.indexOf(tsk), 1);
      },
    },
  }
</script>


<style lang="sass">
  #app
    display: flex
    flex-direction: column 
    margin: auto
    width: 20em
    padding: 2vw

  .ui.checkbox.task
    margin-top: 1.5vw
    display: flex
    justify-content: space-between
    font-size: 16px
</style>
