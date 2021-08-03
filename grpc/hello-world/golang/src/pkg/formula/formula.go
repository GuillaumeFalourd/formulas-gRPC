package formula

import (
	"context"
	"log"
	"os"
	"time"

	pb "github.com/GuillaumeFalourd/poc-grpc-golang/helloworld"

	"google.golang.org/grpc"
)

const (
	address     = "localhost:3009"
	defaultName = "world"
)

type Formula struct {
	Text string
}

func (f Formula) Run() {
	// Set up a connection to the server.
	conn, err := grpc.Dial(address, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewGreeterClient(conn)

	// Contact the server and print out its response.
	name := f.Text
	if len(os.Args) > 1 {
		name = os.Args[1]
	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	// Call SayHello method through gRPC.
	r, err := c.SayHello(ctx, &pb.HelloRequest{Name: name})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %s", r.GetMessage())

	// Call SayHelloAgain method through gRPC.
	r, err = c.SayHelloAgain(ctx, &pb.HelloRequest{Name: name})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %s", r.GetMessage())
}
