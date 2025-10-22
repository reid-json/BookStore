<script>
export default{
  name: "BookPage",
  data(){
    return{
      books: []
    };
  },
  mounted(){
    fetch('http://127.0.0.1:8000/api/books/')
        .then(res => res.json())
        .then(data => {
          console.log("Book data", data);
          this.books = data;
        })
        .catch(err => console.error('API error: ', err));

}
};
</script>

<template>
  <div>
    <h1>Welcome to the Books Page</h1>
    <ul>
      <!-- This basically loops the table of books and lists them in this format -->
      <li style = "list-style: none;" v-for = "books in books" :key="books.id">
        <!-- This is the format section -->
        <p>{{ books.title}}</p>
        <p>{{ books.author}}</p>
        <p>{{ books.price}}</p>
        <p>{{ books.published_date}}</p>
        <p>{{ books.stock}}</p>

      </li>

    </ul>
  </div>
</template>

<style scoped>

</style>