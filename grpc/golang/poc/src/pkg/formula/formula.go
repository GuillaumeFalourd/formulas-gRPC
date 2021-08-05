// This is the formula implementation class.
// Where you will code your methods and manipulate the inputs to perform the specific operation you wish to automate.

package formula

import (
	"context"
	"log"
	"time"

	"google.golang.org/grpc"

	pb "formula/pkg/formula/protos/user"
)

const (
	address     = "localhost:9090"
	defaultName = "world"
)

type Formula struct {
	Username string
	Password string
}

func (f Formula) Run() {

	// Set up a connection to the server.
	conn, err := grpc.Dial(address, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewUserClient(conn)

	// Call server Login method through gRPC.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.Login(ctx, &pb.LoginRequest{Username: f.Username, Password: f.Password})
	if err != nil {
		log.Fatalf("Unexpected Error: %v", err)
	}

	// Print response outputs
	log.Printf("Response Message: %s", r.Responsemessage)
	log.Printf("Response Code: %d", r.ResponseCode)
}
