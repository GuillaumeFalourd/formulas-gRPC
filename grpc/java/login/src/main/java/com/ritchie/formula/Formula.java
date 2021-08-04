package com.ritchie.formula;

import com.guillaume.grpc.User.APIResponse;
import com.guillaume.grpc.User.LoginRequest;
import com.guillaume.grpc.userGrpc;
import com.guillaume.grpc.userGrpc.userBlockingStub;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class Formula {

    private final String username;
    private final String password;

    public Formula(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public void Run() {
		ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost",9090).usePlaintext().build();
		// stubs - generate from proto
		userBlockingStub userStub = userGrpc.newBlockingStub(channel);
		LoginRequest loginrequest = LoginRequest.newBuilder().setUsername(username).setPassword(password).build();
		APIResponse response = userStub.login(loginrequest);
		System.out.println(response.getResponsemessage());
    }
}
