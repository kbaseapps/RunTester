task hello_world {
    String name = "World"
    command {
        echo 'Hello, ${name}' > out.txt
    }
    output {
        File out = 'out.txt'
    }
    runtime {
        docker: 'ubuntu:latest'
    }
}

workflow hello {
    call hello_world
}
