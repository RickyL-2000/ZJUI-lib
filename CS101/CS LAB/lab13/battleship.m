n = 5;
playerGrid = zeros(n,n);
playerShots = zeros(n,n);
computerGrid = zeros(n,n);
computerShots = zeros(n,n);
shipsAvailable = [ 4 4 ];
for shipIndex = 1:numel( shipsAvailable ) %Loop through the ships available
    shipLength = shipsAvailable( shipIndex ); %Get the length of a ship
    shipNotPlaced = 1;
    while shipNotPlaced
        % Generate a random position and orientation for the ship.
        shipOrientation = randi(2);
        if shipOrientation == 1  % horizontal
            %n is grid-length, 
            %n - shiplength => possible positions to choose from
            shipLayoutStart = randi( n-shipLength ); 
            %ship starting x-point to ending x-point
            shipLayoutX = shipLayoutStart:shipLayoutStart + shipLength - 1;
            %ship 
            shipLayoutY = randi( n ) * ones( shipLength );
        else  % vertical
            shipLayoutStart = randi( n-shipLength );
            shipLayoutX = randi( n ) * ones( shipLength );
            shipLayoutY = shipLayoutStart:shipLayoutStart+shipLength-1;
        end %if

        % Attempt to place the ship on the grid.  If there is a conflict, then loop back.
        shipPosnOK = 1; %just a variable to change if position of a ship is ok
        % find positions in playerGrid with non-zero and save them in shipsX, shipsY
        [ shipsX, shipsY ] = find( playerGrid );
        for shipIdx = 1:max( numel( shipsX ),numel( shipsY ) )
            for idx = 1:shipLength
                % compare possible new ship positions with current ship
                % positions on the playerGrid
                if shipLayoutX( idx ) == shipsX( shipIdx ) && shipLayoutY( idx ) == shipsY( shipIdx )
                    shipPosnOK = 0;
                    break;
                end %if
            end %for
            if ~shipPosnOK
                %break out of shipIdx loop
                break;
            end %if
        end %for
        if shipPosnOK
            playerGrid( shipLayoutX,shipLayoutY ) = shipLength;
            shipNotPlaced = 0;
        end %if
    end %while
end %for
%disp( playerGrid );
%disp( playerShots );


% Repeat the process for `computerGrid`.
for shipIndex = 1:numel( shipsAvailable ) %Loop through the ships available
    shipLength = shipsAvailable( shipIndex ); %Get the length of a ship
    shipNotPlaced = 1;
    while shipNotPlaced
        % Generate a random position and orientation for the ship.
        shipOrientation = randi(2);
        if shipOrientation == 1  % horizontal
            %n is grid-length, 
            %n - shiplength => possible positions to choose from
            shipLayoutStart = randi( n-shipLength ); 
            %ship starting x-point to ending x-point
            shipLayoutX = shipLayoutStart:shipLayoutStart + shipLength - 1;
            %ship 
            shipLayoutY = randi( n ) * ones( shipLength );
        else  % vertical
            shipLayoutStart = randi( n-shipLength );
            shipLayoutX = randi( n ) * ones( shipLength );
            shipLayoutY = shipLayoutStart:shipLayoutStart+shipLength-1;
        end %if

        % Attempt to place the ship on the grid.  If there is a conflict, then loop back.
        shipPosnOK = 1; %just a variable to change if position of a ship is ok
        % find positions in playerGrid with non-zero and save them in shipsX, shipsY
        [ shipsX, shipsY ] = find( computerGrid );
        for shipIdx = 1:max( numel( shipsX ),numel( shipsY ) )
            for idx = 1:shipLength
                % compare possible new ship positions with current ship
                % positions on the playerGrid
                if shipLayoutX( idx ) == shipsX( shipIdx ) && shipLayoutY( idx ) == shipsY( shipIdx )
                    shipPosnOK = 0;
                    break;
                end %if
            end %for
            if ~shipPosnOK
                %break out of shipIdx loop
                break;
            end %if
        end %for
        if shipPosnOK
            computerGrid( shipLayoutX,shipLayoutY ) = shipLength;
            shipNotPlaced = 0;
        end %if
    end %while
end %for
% 2. Game grid setup
%%% You should have this part filled in from above

% 3. Ship setup
%%% You should have this part filled in from above

% 1. Main loop
gameOver = 0;
while ~gameOver
    input( 'Press any key to start your turn ' );
    clc
    disp( 'Your ships locations:' );
    disp( playerGrid );
    disp( 'Your shots made' );
    disp( playerShots );
    disp('Computer ships');
    disp( computerGrid );  % useful to see both sides for debugging
    disp('Computer shots');
    disp( computerShots );  % useful to see both sides for debugging
    
    % Get player action.
    shots = input( 'Give me a coordinate pair in [x,y]: ' );   %input like "[1 1]"
    shotX = shots( 1 );
    shotY = shots( 2 );

    % Update the grid with the shot. (4.)
    [ computerGrid, hit ] = evaluateShot( computerGrid,shotX,shotY );
    [ playerShots ] = evaluateGuess( playerShots,shotX,shotY,hit );
    if hit
        disp( "You hit a ship!" ); % change this msg when computer is playing
    end %if
    
    % Check for victory. (5.)
    if checkLoss( computerGrid )
        gameOver = 1;
        disp( 'You have won the game!' );
        break;
    end %if
    
    % Get computer action. (6.)
    disp( 'Computer is playing...' );
    [ shotX ,shotY ] = getComputerShots( computerShots );
    
    % Update the grid with the shot. (4.)
    % Fill this part by changing the code above
    [ playerGrid, hit ] = evaluateShot( playerGrid,shotX,shotY );
    [ computerShots ] = evaluateGuess( computerShots,shotX,shotY,hit );
    if hit
        disp( "AlphaBa hit a ship!" ); % change this msg when computer is playing
    end %if
    % Check for victory. (5.)
    % Fill this part by changing the code above
    if checkLoss( playerGrid )
        gameOver = 1;
        disp( 'You have lost the game!' );
        break;
    end %if
    
    
    disp( 'Computer Finished' );    
end %while