class LineCalculator

    attr_reader :lines, :grid

    def initialize
        @lines = []
        @grid = []
    end

    def add_line(input)
        @lines.push(input)
    end

    def add_straight_line(input)
        if LineCalculator.check_straight_line(input)
            @lines.push(input)
        end
    end

    def get_empty_grid
        all_x_values = @lines.map { |line| [line[0][0], line[1][0]] }
        max_x_values = all_x_values.flatten().max + 1
        all_y_values= @lines.map { |line| [line[0][1], line[1][1]] }
        max_y_values = all_y_values.flatten().max + 1
        @grid = Array.new(max_y_values) { Array.new(max_x_values) }
    end

    def add_point(x, y)
        if @grid[y][x] == nil
            @grid[y][x] = 1
        else
            @grid[y][x] += 1
        end
    end

    def draw_line(line)
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 == x2
            # it's a vertical line
            start, finish = [y1, y2].minmax()
            y = start
            while y <= finish
                self.add_point(x1, y)
                y += 1
            end
        elsif y1 == y2
            # it's a horizontal line
            start, finish = [x1, x2].minmax()
            x = start
            while x <= finish
                self.add_point(x, y1)
                x += 1
            end
        else
            # it's a diagonal line
            # start with whichever is furthest left, then judge whether it's up right or down right 
            x1_is_start = x1 < x2

            if x1_is_start
                # x1 is furthest on the left
                x = x1
                y = y1
                if y2 > y1
                    # down-right line
                    while x <= x2
                        self.add_point(x, y)
                        x += 1
                        y += 1
                    end
                elsif y1 > y2
                    # up-right line
                    while x <= x2
                        self.add_point(x, y)
                        x += 1
                        y -= 1
                    end
                end
            else
                # x2 is furthest on the left, start there
                x = x2
                y = y2
                if y1 > y2
                    # down-right line from x2, y2 - x1, y1
                    while x <= x1
                        self.add_point(x, y)
                        x += 1
                        y += 1
                    end
                elsif y2 > y1
                    # up-right line from x2, y2 - x1, y1 
                    while x <= x1
                        self.add_point(x, y)
                        x += 1
                        y -= 1
                    end
                end
            end            
        end
    end

    def draw_grid
        @lines.each { |line| self.draw_line(line) }
        @grid
    end

    def get_points_with_2_or_more()
        def get_total_for_row(row)
            row.count { |num| num != nil and num >= 2 }
        end
        total = 0
        @grid.each { |row| total += get_total_for_row(row) }
        total
    end

    def self.check_straight_line(input)
        x1, y1 = input[0]
        x2, y2 = input[1]
        x1 == x2 or y1 == y2
    end
end